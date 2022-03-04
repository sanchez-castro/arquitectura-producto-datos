# Class 6 Lab: Data Warehouses & ELT

## Objectives
- Configure the following GCP architecture:
    - GCS Bucket
    - VMs with read/write access to GCS Bucket
    - Bigquery External Tables reading from GCS Bucket
- Write API Request Payloads to GCS Bucket from Python
- Parse Payload via SQL in Data Warehouse

## Requirements
We will be performing most of this lab in GCP. An active Google Cloud Project will be needed in order to follow along. We will be using the following services:

- [AI Platform Notebooks](https://cloud.google.com/vertex-ai-workbench)
- [Google Cloud Storage](https://cloud.google.com/storage)
- [IAM & Admin: Service Accounts](https://cloud.google.com/iam/docs/service-accounts)
- [Google Bigquery](https://cloud.google.com/bigquery)

Utilizing AI Platform VMs will enable us to skip installing dependent python libraries.

We will also be using the [WeatherAPI](https://www.weatherapi.com/). While not required, it is recommended to sign up for a free account to acquire an API Key and follow along with the lab.

## Lab
In this lab, we will be finishing up with the WeatherAPI by writing an ELT job. We'll also be completing this process entirely in The Cloud. The process will be as follows:

- Make GET requests to the Historical Weather Endpoint
- Augment with some additional fields for easier parsing
- Write the request payloads to a GCS bucket directly, without saving the data to our VM
- Parse the weather data in Google Bigquery to create new tables and complete our ELT job

To make this easier for ourselves, we'll explore some patterns for assigning permissions to our cloud services.

### I. Configure GCP Architecture
#### A. Create GCS Bucket
1. Navigate to the [GCS Browser](https://console.cloud.google.com/storage/browse)
2. Select Create Bucket
3. Name your bucket
  - This must be a globally unique name
4. Choose where to store your data
  - For this demo, we will be selecting single region availability
  - I will choose us-central1 for environmental reasons
5. Choose a default storage class
  - Select Standard
6. Choose how to control access to objects
  - Select `Enforce public access prevention on this bucket`. This will restrict access to your bucket on the public Internet.
  - Select Uniform Access Control
7. Press Create

#### B. Create AI Platform Notebook
1. Navigate to the [AI Platform Dashboard](https://console.cloud.google.com/ai-platform/dashboard)
2. Select View Notebook Instances
3. Select New Notebook
4. Select Advanced Options
5. Enter a Name and Zone for your notebook
  - Region: us-central1
  - Zone: us-central1-a
6. Environment
  - OS: Debian 10
  - Environment: Python 3 (with Intel MKL)
7. Machine Configuration
  - Machine Type: n1-standard-1
8. Press Create

#### C. Provide Read Access on Bucket to VM
1. Navigate to the [Service Account Dashboard](https://console.cloud.google.com/iam-admin/serviceaccounts) for your project
2. Select the Compute Engine default service account
3. Select Keys
4. Select ADD KEY
  - Select Create New Key
  - Select JSON
  - Press CREATE
5. Hold on to the downloaded JSON file
6. Navigate back to your storage bucket
7. Select Permissions
  - Select +ADD
  - Principals: Enter the name of your compute engine default service account
  - Select a role: provide bucket and object editor access
8. Return to the navigation page for your bucket
9. Select Create Folder
  - Name: auth
10. Upload the Service Account Key File to your auth folder

### Write API Request Payloads to GCS Bucket from Python

First, we can open a Jupyter Lab window directly from the UI for AI Platform:
1. Navigate to the [AI Platform Instance List](https://console.cloud.google.com/vertex-ai/workbench/list/instances)
2. If your instance isn't on, START it.
3. Select `JupyterLab`

Now, to ensure we can always access our GCS Bucket, we'll need to copy the service account credentials we stored there. We can do this by opening a new terminal window and runing the following:

```shell
mkdir /.auth && gsutil cp <key file path> /.auth
```

This code creates a hidden auth folder and copies our key to that location. Now we can set an environment variable that exposes the location of our key file to python modules that make requests to the Storage API.

```shell
export GOOGLE_APPLICATION_CREDENTIALS="<KEY_PATH>"
```

Great. Now that we have our access provisioned, lets go about making our typical GET requests to the Weather API.

This time around, we'll be writing the results directly to our GCS Bucket. This [Stack Overflow](https://stackoverflow.com/questions/43264664/creating-uploading-new-file-at-google-cloud-storage-bucket-using-python) thread has some useful tips for using GCS Storage Blobs. I would recommend reading it.

We will be writing all of the code for this section live. My solutions will be posted after class.

### Parse Payload via SQL in Data Warehouse
Now that we've written our request payloads to GCS, we'll set up an [External Table](https://cloud.google.com/bigquery/external-data-cloud-storage) in BigQuery to parse it.

1. Navigate to the [Bigquery Console](https://console.cloud.google.com/bigquery)
2. Find your current project under the pinned projects section
3. Click on the menu (three dots) and select "Create dataset"
  - Dataset ID: weather
  - Select "CREATE DATASET"
4. Click on the menu button for your data set and select "Create Table "
  - Create table from: Google Cloud Storage
  - Table Type: External table
  - File format: JSON
  - Select file from GCS Bucket: weather/*

Now that we have our External Table set up, we'll be parsing our weather data in the Bigquery Cloud Console via SQL to complete our ELT job.
