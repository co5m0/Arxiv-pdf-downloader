import csv
import requests
import json
import os
import sys
import tarfile
from multiprocessing import Pool, cpu_count
import urllib.request


base_url = 'https://archive.org/download'

# def download_and_extract(path):
#     response_tar = requests.get('{}/{}/{}.tar\n'.format(base_url,path,path))
#     tar = tarfile.open('{}.tar'.format(path)

def download_file(file,url):
    file_tmp = urllib.request.urlretrieve(url, filename=None)[0]

def main():
    print(cpu_count())
    number_of_id = sys.argv[1]

    subject_counter = dict()


    json_url = 'https://archive.org/advancedsearch.php?q=mediatype%3A%28texts%29+AND+collection%3A%28arxiv%29&fl%5B%5D=identifier&fl%5B%5D=subject&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows={}&page=1&output=json'.format(number_of_id)

    out_file = 'index.txt'
    subject_csv = 'subjects.csv'
    output_folder = './INPUT'
    req = requests.get(json_url)
    json_obj = json.loads(req.text)

    with open(out_file, "w") as code:
        for obj in json_obj['response']['docs']:
            print(obj)
            id = obj['identifier']
            code.write('{}/{}/{}.pdf\n'.format(base_url,id,id[6:]))
            for subs in obj['subject']:
                print(subs)
                subject_counter.setdefault(subs,0)
                subject_counter[subs] += 1
            # response_tar = requests.get('{}/{}/{}.tar\n'.format(base_url,id['identifier'],id['identifier']))
            # download_and_extract(id['identifier'])
            # print(download_file(id['identifier'],'{}/{}/{}.tar\n'.format(base_url,id['identifier'],id['identifier'])))
    with open(subject_csv, "w") as csvfile:
        fieldnames = ['subject', 'occurency']
        spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        spamwriter.writeheader()
        for subs in subject_counter:
            spamwriter.writerow({'subject':subs, 'occurency':subject_counter[subs]})
            # spamwriter.writerow([subs,subject_counter[subs]])
    print(subject_counter)

    try:
        os.mkdir(output_folder)
    except OSError:
        print ("Creation of the directory %s failed" % output_folder)
    except Exception as e:
        print (e)
    else:
        print ("Successfully created the directory %s " % output_folder)


if __name__ == '__main__':
    main()
