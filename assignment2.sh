#!/bin/bash

#run through given arguments and get the file name
while getopts ":f:" opt; do
  case $opt in
    f) file="$OPTARG" ;;
    *)
      echo "Usage: $0 [-f file]"
      exit 1
      ;;
  esac
done

#upload the file to the Azure Storage Blob container using the provided SAS token
az storage blob upload \
  --account-name sacodeassessment \
  --container-name results \
  --name ingest-assessment-20260210-MC/"$file" \
  --file "$file" \
  --sas-token "sv=2022-11-02&ss=b&srt=o&sp=wc&se=2034-11-11T11:00:00Z&st=2024-11-10T23:00:00Z&spr=https&sig=D%2BgRbWPJDTmsbPtyfTEiTnb7gg594uNsvm62oQK49Yg%3D"