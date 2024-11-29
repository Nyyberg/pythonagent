import sys
from autogen import AssistantAgent
from autogen import UserProxyAgent

configList = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
]

assistant = AssistantAgent(
    name ="assistant",
    llm_config={
        "config_list": configList,
        "temperature": 0,
    },
    system_message="YOU ARE A CODING ASSISTANT THAT HELPS SOLVE PROBLEMS WITH PYTHON SOLUTIONS. DO NOT INCLUDE MULTIPLE CODE BLOCKS IN ONE RESPONSE. IF YOU WANT THE USER TO SAVE THE CODE IN A FILE PUT # filename: <filename> AS THE FIRST LINE. WHEN EVERYTHING HAS BEEN RUN AND EVERYTHING WORKS REPLY WITH TERMINATE"
)

user_proxy = UserProxyAgent(
    name="userproxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x:x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "code", "use_docker": False},
)

reply = user_proxy.initiate_chat(
    assistant,
    message="""{}""".format(sys.argv[1]),
    summary_method="reflection_with_llm"
)