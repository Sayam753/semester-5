This is the submission of the Assignment-1 of creating an inverted index.

Approach followed -
1. Scan through all the files.
2. Remove digits and punctuation.
3. Create document frequency for that file.
4. Remove stop words.
5. Load the posting list and then update it.
6. Save the posting list in JSON format.
7. Generate the output file in txt format.

Data Structures - 
1. Dictionary for vocab list.
2. List of tuples for posting list.

Space Complexity - O((Size of vocab list)*(Size of their posting lists))

Time Complexity - O((Number of files)*(Number of words)*log(Number of words))
                - (Number of words)*log(Number of words) for Dictionary

Thanks
Name - Sayam Kumar
Roll Number - S20180010158
Email ID - sayam.k18@iiits.in