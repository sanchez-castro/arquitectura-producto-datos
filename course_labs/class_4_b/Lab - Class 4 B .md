# Lab - Class 4 B

Fecha: February 15, 2022
Professor: Adrian
Tipo: 🔍 Lab
Tópico: APIs for accessing Services

# LAB: API as Service

[APIs Review](https://www.notion.so/APIs-Review-61125f3cc8cb48aba2c520bce6e22ac1)

Google Cloud [GCP API Explorer](https://console.cloud.google.com/apis/library): API Library / API Dashboard

---

## Cloud Storage JSON API

The Cloud Storage JSON API is a simple, JSON-backed interface for accessing and manipulating Cloud Storage projects in a programmatic way.

Use the [curl](https://curl.haxx.se/) CLI tool to make an HTTP POST method request. Pass in the `values.json` file into the request body. Pass the OAuth token and a JSON specification as request headers. This request will be routed to the Cloud Storage endpoint, which contains a query string parameter set to your Project ID.

1. Enable Cloud Storage API
[`https://console.cloud.google.com/apis/library/storage-api.googleapis.com`](https://console.cloud.google.com/apis/library/storage-api.googleapis.com)
2. Create a json file with metadata
 
  -In GCP console, Open a terminal (there is a symbol in the upper-right side of the screen) 
  -We are going to create a bucket, please replace <YOUR_BUCKET_NAME> with a name of a bucket that does not exists.

```bash
nano values.json
```

```bash
{  "name": "<YOUR_BUCKET_NAME>",
   "location": "us",
   "storageClass": "multi_regional"
}
```

1. Authentication & Authorization
- *Authentication* refers to the process of determining a client's identity.
- *Authorization* refers to the process of determining what permissions an authenticated client has for a set of resources.
1. Open the [OAuth 2.0 playground](https://developers.google.com/oauthplayground/)
Scroll down and select **Cloud Storage API V1**. 
Select the **https://www.googleapis.com/auth/devstorage.full_control** scope
Click on the blue box that says **Authorize APIs**.
Select your username and then click **Allow** when prompted for permissions.
Click on **Exchange authorization code for tokens**.
**Copy** the access token, it will be used in the following step.
2. In the shell

```bash
export OAUTH2_TOKEN=<YOUR_TOKEN>
export PROJECT_ID=<YOUR_PROJECT_ID>
```

```bash
curl -X POST --data-binary @values.json \
    -H "Authorization: Bearer $OAUTH2_TOKEN" \
    -H "Content-Type: application/json" \
    "https://www.googleapis.com/storage/v1/b?project=$PROJECT_ID"
```

1. Upload an image to the Cloud Shell Terminal
2. Get the image path

```bash
realpath image-name.png/jpg
```

1. Export to shell variable and hit the API

```bash
export OBJECT=<DEMO_IMAGE_PATH>
export BUCKET_NAME=<YOUR_BUCKET>
```

```bash
curl -X POST --data-binary @$OBJECT \
    -H "Authorization: Bearer $OAUTH2_TOKEN" \
    -H "Content-Type: image/png" \
    "https://www.googleapis.com/upload/storage/v1/b/$BUCKET_NAME/o?uploadType=media&name=demo-image"
```

---

### Cloud Vision API

Cloud Vision allows developers to easily integrate vision detection features within applications, including image labeling, face and landmark detection, optical character recognition (OCR), and tagging of explicit content.

1. Create a bucket with fine grained access
2. Upload image
3. Give granular permissions to the object in `Edit Access` section. 
    1. public + allUsers + reader
4. Enable Cloud Vision API service 
5. Open the API explorer in [`https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate?apix=true`](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate?apix=true)
6. Build the API POST request with:
    1. Click inside of the curly braces in the Request body field. You'll be asked to select a property - choose "requests". This will generate the next level. Click inside the brackets and click the blue plus sign icon, select `[Add Item]` - for your property select "features".
    2. Inside "features" click inside the curly brace, click the blue plus icon and select `[Add Item]`, select "type"; next to it select LABEL_DETECTION.
    3. You should have the blue plus icon at the end of the "features" block where you can choose to add "image"; then add "source", and "imageUri". Next to "imageUri" enter the path to the image file in your bucket. The path should look like this: `gs://MY_BUCKET/demo-image.jpg`

---

### Cloud Natural Language API

Provides natural language understanding technologies, such as sentiment analysis, entity recognition, entity sentiment analysis, and other text annotations, to developers.

1. Export variable

```bash
# dedefine gcp project variable
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value core/project)
```

1. Create service account

```bash
gcloud iam service-accounts create my-natlang-sa --display-name "my natural language service account"
```

1. Create key to log in as your new service account

```bash
gcloud iam service-accounts keys create ~/key.json \
  --iam-account my-natlang-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com
```

1. Define de key.json as credential

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/USER/key.json"
```

API usage

```bash
gcloud ml language analyze-entities --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'." > result.json
```

---

## Service Accounts

A service account is a special Google account that belongs to your application or a [virtual machine](https://cloud.google.com/compute/docs/instances/) (VM) instead of an individual end user. Your application uses the service account to [call the Google API of a service](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#authorizingrequests), so that the users aren't directly involved.

For example, a Compute Engine VM may run as a service account, and that account can be given permissions to access the resources it needs. This way the service account is the identity of the service, and the service account's permissions control which resources the service can access.

A service account is identified by its email address, which is unique to the account.

### **User-managed service accounts**

Compute engine service account

`PROJECT_NUMBER-compute@developer.gserviceaccount.com`

App engine service account

`PROJECT_ID@appspot.gserviceaccount.com`

### Google-managed service accounts

Google API service account

`PROJECT_NUMBER@cloudservices.gserviceaccount.com`

## Creating a service accounts

Creating a service account is similar to adding a member to your project, but the service account belongs to your applications rather than an individual end user.

```bash
gcloud iam service-accounts create my-sa-123 --display-name "my service account"
```

## Granting Roles to Service Accounts

When granting IAM roles, you can treat a service account either as a [resource](https://cloud.google.com/iam/docs/overview#resource) or as an [identity](https://cloud.google.com/iam/docs/overview#concepts_related_to_identity).

**Granting roles to a service account for specific resources**

```bash
gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
    --member serviceAccount:my-sa-123@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com --role roles/editor
```

When an identity calls a Google Cloud API, Google Cloud Identity and Access Management requires that the identity has the appropriate permissions to use the resource. You can grant permissions by granting roles to a user, a group, or a service account.

There are three types of roles in Cloud IAM:

- **Primitive roles**, which include the Owner, Editor, and Viewer roles that existed prior to the introduction of Cloud IAM.
- **Predefined roles**, which provide granular access for a specific service and are managed by Google Cloud.
- **Custom roles**, which provide granular access according to a user-specified list of permissions.

## Exercise

1. Create Service account + Roles 
2. Create a VM instance + specific service account
3. Prepare machine

```bash
# install virtualenv
sudo apt-get update
sudo apt-get install -y virtualenv
virtualenv -p python3 venv
source venv/bin/activate

#install pip and libraries
sudo apt-get install -y git python3-pip
pip install google-cloud-bigquery
pip install pyarrow
pip install pandas
```

1. Python file

```bash
echo "
from google.auth import compute_engine
from google.cloud import bigquery
credentials = compute_engine.Credentials(
    service_account_email='**YOUR_SERVICE_ACCOUNT**')
query = '''
SELECT
  year,
  COUNT(1) as num_babies
FROM
  publicdata.samples.natality
WHERE
  year > 2000
GROUP BY
  year
'''
client = bigquery.Client(
    project='**YOUR_PROJECT_ID**',
    credentials=credentials)
print(client.query(query).to_dataframe())
" > query.py
```

1. Update script with Project ID

```bash
sed -i -e "s/YOUR_PROJECT_ID/$(gcloud config get-value project)/g" query.py
```

 6. Update script with service account

```bash
sed -i -e "s/YOUR_SERVICE_ACCOUNT/bigquery-qwiklab@$(gcloud config get-value project).iam.gserviceaccount.com/g" query.py
```

1. Run the script

```bash
python query.py
```

[Overview | Cloud IAM Documentation | Google Cloud](https://cloud.google.com/iam/docs/overview#concepts_related_to_identity)

[Smart Analytics, Machine Learning and AI on Google Cloud | Google Cloud Skills Boost](https://www.cloudskillsboost.google/course_templates/55)

---

**[Exploring APIs](https://www.cloudskillsboost.google/quests/54)**

[1. Introduction to APIs in Google](https://www.cloudskillsboost.google/catalog_lab/1342)

[2. Cloud vision API](https://www.cloudskillsboost.google/catalog_lab/1241)

[3. Cloud Natural Language API: Qwik Start](https://www.cloudskillsboost.google/catalog_lab/709)

[4. Service Accounts and Roles: Fundamentals](https://www.cloudskillsboost.google/catalog_lab/956)
