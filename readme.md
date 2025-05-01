Originally from the [cvp-mcp-demo](https://github.com/burnyd/mcp-server-cvp-demo) repo. 

## To also note this is not official only a simply demo

I plan to add some more of our [resource API's](https://aristanetworks.github.io/cloudvision-apis/) for this to leverage as demos in the near term future.

The changes here are the following.
- Proper uv usage
- Leverages Langchain [MCP toolkit adapter](https://github.com/langchain-ai/langchain-mcp-adapters)
- Gemini 2.5 as the LLM

So like the previous demo this no longer has the necessity of Claude desktop.

### To make this run

Please add a .env file like the following.

```bash
CVPTOKEN="Somesupersecuretoken"
CVP="www.arista.io"
```

Install uv unless you already have it.

```bash
pipx install uv

```

### Get a gemini token 

[Here](https://aistudio.google.com/app/apikey) and save your api key as 

```bash
GEMINI_API_KEY="KeyIGotFromGoogleAPIkey"
```


### uv

install the requirements for this project

```bash
uv pip install -r pyproject.toml
```

run the file. 

```bash
uv run python3.13 cvmcpclient.py
```

Result

```bash
Welcome to the chat! Type 'exit' to quit.
You: tell me about my clouvsion inventory and how many devices I have?  Can you give this to me in a table like format?
Processing request of type CallToolRequest
HTTP Request: GET https://www.arista.io/api/resources/inventory/v1/Device/all "HTTP/1.1 200 OK"
HTTP Request: GET https://www.arista.io/api/resources/inventory/v1/Device/all "HTTP/1.1 200 OK"
The final answer is: OK. I can get the inventory of your devices from CloudVision.

Here is your CloudVision inventory:

| Hostname       | Model             | Software Version   | Device ID                            |
| :------------- | :---------------- | :----------------- | :----------------------------------- |
| xxx            | DCS-7280CR2A-30   | 4.30.5M            |                                      |
| xxx            | DCS-7280CR2A-30   | 4.30.5M            |                                      |
| xxx            | DCS-7280CR2A-30   | 4.30.5M            |                                      |
| xxx            | DCS-7280CR2A-30   | 4.30.5M            |                                      |
| xxx            | DCS-7050SX3-48YC8 | 4.30.5M            |                                      |
| xxx            | DCS-7050SX3-48YC8 | 4.32.0F            |                                      |
| xxx            | DCS-7050SX3-48YC8 | 4.30.5M            |                                      |
| xxx            | DCS-7050SX3-48YC8 | 4.30.5M            |                                      |
| xxx            | DCS-7804-CH       | 4.32.2.1F          |                                      |
| xxx            | DCS-7804-CH       | 4.32.2.1F          |                                      |
| DC1_LEAF1A     | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825601     |
| DC1_LEAF1B     | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825602     |
| DC1_L2_LEAF2A  | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825603     |
| DC1_L2_LEAF2B  | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825604     |
| DC1_SVC2B      | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825606     |
| DC1_SVC2A      | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825605     |
| DC1_SPINE2     | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825699     |
| DC1_SPINE1     | cEOSLab           | 4.33.1F            | 1C68470A1E0CD6EF7418D78A95825698     |

You have a total of 18 devices in your inventory.

```

## Troubleshooting

The asyncmain.py file if you run this it will essentially do sort of the same entirely outside of MCP.  So if you have the correct cvaas/cvp server as well as API key you should be good here.

```bash
python3 asyncmain.py
```