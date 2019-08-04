import json

outputJSON = {
	'participants': [],
	'messages': [],
}

def removeDuplicateMessages(filepath):

	with open(filepath, encoding="utf8") as json_file:
		data = json.load(json_file)

		print("Message in " + filepath + ": " + str(len(data['messages'])) )

		for person in data['participants']:
			if person['name'] not in outputJSON['participants']:
				outputJSON['participants'].append({'name': person['name']})
		
		uniqueMessages = set()
		for message in data['messages']:
			# Convert the JSON object to a string before adding to set
			uniqueMessages.add( json.dumps(message) )
		
		print("Unique Messages in " + filepath + ": " + str(len(uniqueMessages)) + "\n")
		
		for uniqueMessage in uniqueMessages:
			# Covert the JSON string back to JSON before appending to output
			outputJSON['messages'].append( json.loads(uniqueMessage) )
		
def writeToFile(outputFile):
	if not outputJSON['messages']:
		print("There are no messages in the output list!")
		return

	# Sort the messages by timestamp (most recent first)
	outputJSON['messages'].sort(key=lambda message: -message['timestamp_ms'])
	
	with open(outputFile, 'w', encoding='utf8') as output:
		json.dump(outputJSON, output, ensure_ascii=False, indent=4)
	
	print("Written to file: " + outputFile)

def main():

	while True:
		filepath = input("Input the path to file or press 'n' to finish: ")
		if filepath == 'n': break
		else: removeDuplicateMessages(filepath)
	
	outputFile = input("Please specify the output file name: ")
	writeToFile(outputFile)

if __name__ == "__main__":
	main()
