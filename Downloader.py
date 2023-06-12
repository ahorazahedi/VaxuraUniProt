import time
import argparse
import os
import requests
from io import StringIO
import zipfile
import pandas as pd
from tqdm import tqdm
from Bio import SeqIO


def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


def get_accession_list(params, headers={"accept": "application/json"}, search_url="https://rest.uniprot.org/uniprotkb/search"):
    params["fields"] = "accession"
    results = []
    response = requests.get(search_url, params=params, headers=headers)
    response_json = response.json()
    results.extend(response_json['results'])

    while True:
        link_header = response.headers.get('Link')

        if link_header:
            next_page_url = link_header.split(';')[0].strip('<>')

            response = requests.get(next_page_url, headers=headers)
            response_json = response.json()
            results.extend(response_json['results'])

        else:
            break

    output = [item['primaryAccession'] for item in results]

    return output


def get_organism_accession_list(organism_id):

    params = {
        "size": 500,
        "query": f"organism_id:{organism_id} AND reviewed:true",
    }

    return get_accession_list(params)


def get_accession_data(accession, fetch_url="https://rest.uniprot.org/uniprotkb/"):
    response_json = requests.get(
        fetch_url + accession, headers={"accept": "application/json"}).json()

    return response_json


def get_location_from_response_json(response_json):

    try:

        list_of_locations_that_protein_exist = []

        if not response_json['comments']:
             return []

        reponse_comments = response_json['comments']




      
        filtered_comments = [item for item in reponse_comments if item.get(
            "commentType") == "SUBCELLULAR LOCATION"]

        if len(filtered_comments) : 
            filterd_items = filtered_comments[0]['subcellularLocations']

            for filterd_item in filterd_items:
                location_temp = filterd_item['location']['value']
                list_of_locations_that_protein_exist.append(location_temp)

        return list_of_locations_that_protein_exist

    except Exception as e:
        # Exception handling code for other exceptions
        print(f"An error occurred: {str(e)}")
        return []


def get_fasta_string(accession_id ,fetch_url = "https://rest.uniprot.org/uniprotkb/" ):
    response_fasta = requests.get(fetch_url + accession_id + ".fasta", headers={"accept": "text/x-fasta"}).text

    fasta_io = StringIO(response_fasta)
    seq_output = ""
    for record in SeqIO.parse(fasta_io, "fasta"):

        seq_output =  str(record.seq)
  
    return seq_output

if __name__== "__main__":


    print("MEOW")

    parser = argparse.ArgumentParser(description="Read File")
    parser.add_argument("--input" , default='./Organisms.txt')
    parser.add_argument("--output" , default='./downloads')

    args = parser.parse_args()

    file_name = args.input
    output_path = args.output

    if not os.path.exists(output_path):
        print("Folder Not Found Create Download Folder")
        os.makedirs(output_path)

    try : 

        with open(file_name , 'r') as file:
            lines = file.readlines()
            for index , line in enumerate(lines[:]) :
                output_final = []
                parsed_line = line.split(',')
                organism_name = parsed_line[0]
                organism_id = parsed_line[1]
                organism_cat = parsed_line[2][:-1]


                if os.path.exists(f"./downloads/{organism_id}.csv"):
                     print(f"File for Organism , {organism_id} Exist Pass From that Organism")
                     continue
                
                for accession_id in tqdm(get_organism_accession_list(int(organism_id))[:] , desc=f"[{index+1} / {len(lines)}]"):
                 
                    accession_sequence = get_fasta_string(accession_id)
                    response_json_item = get_accession_data(accession_id)
                    locations = get_location_from_response_json(response_json_item)

                    if len(locations):
                         output_final.append([
                              accession_id , accession_sequence , ", ".join(locations) , organism_id , organism_name , organism_cat
                         ])
    
                data_frame = pd.DataFrame(output_final , columns=['accession_id' , 'sequence' , 'locations' ,'organism_id' ,'organism_name' ,'organism_cat'   ])
                data_frame.to_csv(os.path.join(output_path , f"{organism_id}.csv"))

                print("Sleep For One Minute To Prevent API Request Blockage")
                time.sleep(60)

        zip_folder(output_path , './all.zip')
    except FileNotFoundError:
                print("Input File is Wrong")
    except IOError:
                print("Error Reading File")
