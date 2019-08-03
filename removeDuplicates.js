const fs = require('fs');
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
})

var outputJSON = {
	participants: [],
	messages: [],
};

const removeDuplicateMessages = (filepath) => {
	// Read the file and parse the buffer to JSON
	const buffer = fs.readFileSync(filepath);
	const data = JSON.parse(buffer);
	
	console.log(`Messages in ${filepath}: ${data.messages.length}`);
	
	// Add the participants from the JSON if they do not exist
	data.participants.forEach(person => {
		if ( !outputJSON.participants.includes(person) ) {
			outputJSON.participants.push(person);
		}
	})
	
	// Add all messages to a set
	const uniqueMessages = new Set();
	data.messages.forEach(obj => {
		// Stringify before adding to set
		uniqueMessages.add(JSON.stringify(obj));
	})
	console.log(`Unique Messages in ${filepath}: ${uniqueMessages.size}\n`);
	
	// Push the unique messages to the output object
	uniqueMessages.forEach(message => {
		// Parse to JSON before pushing to output
		outputJSON.messages.push(JSON.parse(message));
	})
}

const writeToFile = (outputName) => {
	fs.writeFile(outputName, JSON.stringify(outputJSON, null, 2), 'utf8', () => {
		console.log(`Done writing file to: ${outputName}`)
	});
}

const promptUser = () => {

	readline.question(`Input the path to file or press 'n' to finish: `, (filepath) => {

		if ( filepath === 'n' ) {
			if ( outputJSON.messages.length ) {
				readline.question(`Specify the output file name: `, (outputName) => {
					writeToFile(outputName)
					readline.close();
				})
			}
			else {
				console.log(`The output array is empty!`)
				readline.close();
			}
			
		} else {
			removeDuplicateMessages(filepath);
			promptUser();
		}
	})

}

const main = () => {
	console.log(`Input most recent files first (message_1.json, then message_2.json, ...)\n`)
	promptUser();
}

main()
