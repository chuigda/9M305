from openai import OpenAI

from cfg import read_config
from prompt import SYSTEM_PROMPT_MESSAGE


def main(args):
    config_file_name = args[1]
    config = read_config(config_file_name)
    access_point = config['access_point']
    api_key = config['api_key']

    client = OpenAI(
        api_key=api_key,
        base_url='https://ark.cn-beijing.volces.com/api/v3'
    )

    messages = [SYSTEM_PROMPT_MESSAGE]

    while True:
        user_input = input('User> ')
        user_input = user_input.strip()

        if user_input == ':q' or user_input == ':exit':
            break
        elif user_input == ':c' or user_input == ':continue':
            # let the AI continue the conversation, generate a new sentense
            pass
        else:
            messages.append({
                'role': 'user',
                'content': user_input
            })

        completion = client.chat.completions.create(
            model=access_point,
            messages=messages
        )
        print(completion.choices[0].message.content)

        messages.append({
            'role': 'system',
            'content': completion.choices[0].message.content
        })


if __name__ == '__main__':
    import sys
    main(sys.argv)
