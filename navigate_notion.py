import requests
import cutie

echo "## active_line 2 ##"
def get_page_title(page_id):
echo "## active_line 3 ##"
    url = f\"https://api.notion.com/v1/pages/{page_id}\"
echo "## active_line 4 ##"
    headers = {\"Authorization\": \"Bearer secret_YxVWmqxmRyM2HRitk5s84DPmb6ADWiqPc5VyK2haIxK\", \"Notion-Version\": \"2021-08-16\"}
echo "## active_line 5 ##"
    response = requests.get(url, headers=headers)
echo "## active_line 6 ##"
    data = response.json()
echo "## active_line 7 ##"
    return data[\"properties\"][\"title\"][\"title\"][0][\"plain_text\"]

echo "## active_line 2 ##"
def get_page_children(page_id):
echo "## active_line 3 ##"
    url = f\"https://api.notion.com/v1/blocks/{page_id}/children\"
echo "## active_line 4 ##"
    headers = {\"Authorization\": \"Bearer secret_YxVWmqxmRyM2HRitk5s84DPmb6ADWiqPc5VyK2haIxK\", \"Notion-Version\": \"2021-08-16\"}
echo "## active_line 5 ##"
    response = requests.get(url, headers=headers)
echo "## active_line 6 ##"
    data = response.json()
echo "## active_line 7 ##"
    return data[\"results\"]
