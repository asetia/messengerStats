import json

user_stats = {}
max_reax_messages = []

def parseMessages(messages_filename_full):
    messages_filename = messages_filename_full.split('/')[-1]
    print("Loading messages file '" + messages_filename + "'...")

    with open(messages_filename_full) as json_file:
        data = json.load(json_file)

        for p in data['participants']:
            if p['name'] not in user_stats:
                user_stats[p['name']] = {'sent': 0, 
                                        'laugh_reax_received': 0, 
                                        'laugh_reax_given' : 0}

        for m in data['messages']:
            if m['sender_name'] in user_stats:
                user_stats[m['sender_name']]['sent'] = user_stats[m['sender_name']]['sent'] + 1
                if 'reactions' in m:
                    for r in m['reactions']:
                        # This is a laugh react apparently
                        if r['reaction'] == '\xf0\x9f\x98\x86':
                            user_stats[m['sender_name']]['laugh_reax_received'] = user_stats[m['sender_name']]['laugh_reax_received'] + 1
                            user_stats[r['actor']]['laugh_reax_given'] = user_stats[r['actor']]['laugh_reax_given'] + 1
                    # if len(m['reactions']) == 9 and 'content' in m:
                    #     max_reax_messages.append(m['content'])

def main():

    while True:
        messages_filename_full = input("Please enter the path and filename of the messages file you would like to parse (or n to finish): ")
        if messages_filename_full != 'n':
            parseMessages(messages_filename_full)
            continue
        else:
            break

    print()

    for key in user_stats:
        print(key)
        print("Messages sent: ", user_stats[key]['sent'])
        print("Laugh reax received: ", user_stats[key]['laugh_reax_received'])
        print("Laugh reax given: ", user_stats[key]['laugh_reax_given'])
        print()

    # print("Messages with maximum amount of reax:")
    # for m in max_reax_messages:
    #     print(m)
    #     print()
  
if __name__== "__main__":
    main()
