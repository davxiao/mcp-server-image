# mcp-server-image
A bare minimum MCP server docker image that supports streamable HTTP. This container image can be easily deployed anywhere, e.g. in [GCP Cloud Run](https://cloud.google.com/run).
The Image contains a "hello" tool for testing purposes.

## Build the Container Image
The following can be done in any OS platform but if you plan to deploy the image in Cloud Run, please make sure the final image supports x86 CPU arch as it's required by Cloud Run. If you are not sure, I would recommend running the following steps in [GCP Cloud Shell](https://cloud.google.com/shell).
```
$ git clone https://github.com/davxiao/mcp-server-image.git
$ cd mcp-server-image
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r ./requirements.txt
$ docker build -t hello-mcp .
```
## Host the Container Image
If you plan to deploy in Cloud Run, the easiest way is to host the image in GCP Artifact Registry. First you will need to create a Docker repository and copy the path of the new repo. In this sample the path is `us-docker.pkg.dev/davxiao-test/hello-mcp`
```
$ docker images
  ## The Image ID of the newly built image is shown
$ docker tag 75f06ec7e0e7 us-docker.pkg.dev/davxiao-test/hello-mcp/hello
$ docker us-docker.pkg.dev/davxiao-test/hello-mcp/hello
```
When this is complete, you should see the image shown in the Docker repository you just created.

## Deploy the Container Image
In Cloud Run console, click on "Deploy Container" button and select the container image, make sure the region is chosen correctly, make sure "Require authentication" is selected for security, then make sure container port is "8000" under "Containers, Volumes, Networking, Security", and click on Create button.

In a minute or so, it will prompt the new URL for your new MCP server, the URL will look like this: `https://hello-788968831721.us-central1.run.app`
