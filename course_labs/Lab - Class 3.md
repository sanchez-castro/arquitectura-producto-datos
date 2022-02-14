# Lab - Class 3

Fecha: February 8, 2022
Professor: Adrian
Tipo: 🔍 Lab
Tópico: Google Cloud Platform

[lab class 3](https://docs.google.com/presentation/d/1SIVwWdjvCCPpG9yUtqo-OaeeAjh9sozf-aUI0oRUMYU/edit?usp=drivesdk)

# GCloud Tour

# Google Cloud Credits

[¿Cómo acceder a créditos de Google Cloud Platform?](https://www.notion.so/C-mo-acceder-a-cr-ditos-de-Google-Cloud-Platform-bb888f3eb6c34905b33855bd58ed189b)

# Google Cloud SDK

```bash
gcloud config list
gcloud config list project

glcoud init
gcloud components list 
glcoud components install/update
gcloud auth list

```

[The gcloud tool cheat sheet | Cloud SDK Documentation | Google Cloud](https://cloud.google.com/sdk/docs/cheatsheet#cheat_sheet)

## Google Cloud Storage

Create a storage bucket, upload objects to it, create folders and subfolders in it, and make objects publicly accessible using the Google Cloud command line.

```python
# create a bucket 
gsutil

# list the buckets
gsutil ls

#download an image to local
wget --output-document ada.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Ada_Lovelace_portrait.jpg/800px-Ada_Lovelace_portrait.jpg

#remove image
rm ada.jpg

# download an image from bucket
gsutil cp -r gs://YOUR-BUCKET-NAME/ada.jpg .

# upload to a specific folder in the bucket
gsutil cp gs://YOUR-BUCKET-NAME/ada.jpg gs://YOUR-BUCKET-NAME/image-folder/

# list objects in the bucket
gsutil ls (-l, -r) gs://YOUR-BUCKET-NAME

#change bucket name
gsutil cp -r gs://OLD_BUCKET/* gs://NEW_BUCKET

# make public a file in the bucket
gsutil acl ch -u AllUsers:R gs://YOUR-BUCKET-NAME/ada.jpg

# remove public access
gsutil rm gs://YOUR-BUCKET-NAME/ada.jpg

#change permissions to the bucket
gsutil acl ch -p viewers-838411532074:O gs://YOUR-BUCKET-NAME/
```

[Quickstart: Using the gsutil tool | Cloud Storage | Google Cloud](https://cloud.google.com/storage/docs/quickstart-gsutil)

## Google Compute Engines

### Understanding Regions and Zones

Certain Compute Engine resources live in regions or zones. A region is a specific geographical location where you can run your resources. Each region has one or more zones. For example, the us-central1 region denotes a region in the Central United States that has zones `us-central1-a`, `us-central1-b`, `us-central1-c`, and `us-central1-f`.

Resources that live in a zone are referred to as zonal resources. Virtual machine Instances and persistent disks live in a zone. To attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP.

![Screen Shot 2021-11-01 at 9.20.13 PM.png](Lab%20-%20Class%203%/Screen_Shot_2021-11-01_at_9.20.13_PM.png)

### create

```python
#crate a compute engine with http access

# change root access
sudo su -

#update OS
apt-get update

# install nginx
apt-get install nginx -y

# create a compute engine
gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone us-central1-f

# to see help of commands
gcloud compute instances create --help
```

### start/stop

```bash
#access to VM
gcloud compute ssh machine_name --project "project_name"

#turn on/off a machine
gcloud compute instances start VM_NAME
gcloud compute instances stop VM_NAME

#turn on a machine and run a command
```

[Stopping and starting a VM | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/instances/stop-start-instance#gcloud)

### ssh (secure shell)

```bash
gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME
```

[Connect to Linux VMs | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/instances/connecting-to-instance)
