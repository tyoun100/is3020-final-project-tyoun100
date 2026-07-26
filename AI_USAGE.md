# AI Improvement Record

## Original Development

Explain how you developed the original version and describe any AI assistance used before the first required commit. AI use during this stage should be minimal.
Based on my proposal feedback, I realize I made this project much bigger than I should have. Each part I added that worked
as I wanted it to, I thought of something else that would improve the experience. I did hit a wall of things I could do.
I was unable to figure out how to remove a lot of stuff from the course schedule other than date and assignment. This
really works best when only those two things are pasted.

I developed the original version section by section. I wanted to begin by building class profiles that would hold 
class data. I chose to include professor name and location to help keep everything in one place. From there, I built a
class selection followed by an input for the data. Within the large data entry loop, I slowly expanded what was there
based on errors and additional tests. It started with identifying the date in the beginning of the line and pairing the
assignment that follows. To read ranges, convert abbreviations to numerical values and correct split line issues, Dr.
Wang assisted with errors in my code. To build on that code, I asked AI how to identify a date anywhere in the line, to
which I added the 'move date to front' section. After more testing, I added the merge module with content part. This was
to prevent the module number and its description from being separate assignments. During this later addition, I also 
added remove tabs. Copying the course schedule from IS3020 included the 'what to work on' descriptions. I noticed in my
input they were separated by a tab, so that prevented all of those from being included. At the end of this loop, the 
assignments were saved to their respective classes. The original exception I had here was skipping everything, which I 
fixed accordingly based on Dr. Wang's feedback. However, after marking more additions and changes to tailor my results,
the error description may not be working as intended. For the sorting loop, I knew the only practical usage would be to
have the assignments in order based on due date. I'm not quite sure what {_gititem_} is, but it functions accordingly.
As I'm writing this, I realized I never tested original inputs out of order, but the CSV is sorted and merges classes.
I added dynamic column widths based on the length of the assignment name to prevent issues displaying. I used the
master_schedule next to print the layout I wanted with each header followed by each class and assignment. After many 
tests, I finally added the CSV to write the data and later updated the status changes. I had a few difficulties in this
area. I typically read through the suggested text before pressing tab to accept it in my code. I did this with the read
and write where the csv.writer or dictreader are. That caused errors that were fixed when I asked AI where my error is
based on the error code. I later added a loop to update the status. It was failing initially because I used 'assignment'
when I needed 'task'. I used both throughout for basically the same thing. The last thing I tried to add was the load
function. It gave me a definition error, so I moved the helper functions to the top for load, save and read. There was an
additional definition error then, so I decided to keep the code functioning as is, saving and updating until the program is
ended.

## AI Tools Used

List each AI tool used while improving the application.
Google Gemini

## Improvements Requested

Describe the important prompts or requests you gave the AI. Do not paste a complete chat transcript.

Once the date identification at the front of the line was set up, I attempted another schedule. This one had the date at
the end. I asked AI how to identify the date anywhere in the line. I understand the code itself, but the use of 'i' was
unknown before then.

I needed to remove the sentences with a tab. I asked AI how to identify tab, and it informed me to use '\t'. This was
a small, but important use.

I had difficulty with my dynamic spacing based on assignment lengths. AI added an additional 'max' to the line of code.

A few errors of indents, missing () and wrong terminology (as mentioned for CSV), AI helped with error correction, in
most cases.


## Changes Accepted

For each major accepted change, explain what changed, why you accepted it, and how you verified that you understood it.

For date identification, I originally had date in front being the only way to identify it. AI informed me to use 'i',
which is index or iteration. This line of code is looking for '/' with an index not equal to 0. It finds it as 'i',
then puts 'i' or the date in the front and the text previously in the front to the back, reorganizing the line with a 
temporary placeholder. I accepted this because it worked perfectly for the assignments I tested.

For the additional 'max' on the dynamic column widths, I accepted it. Looking at the code more closely, I realized I had
a minimum length as well as a maximum. The inner max found the maximum number. The outer max then took the higher of 
the two numbers.


## Changes Rejected or Revised

Describe any AI suggestion you rejected or modified and explain why.

During an error identification, AI suggested using chain of row.get in the CSV area. I remember from the course modules
less complicated ways to form a simple CSV.

During another error identification, AI said my code needed to include 'p' and 'c' within the line. I had no idea what
those would be doing, so I continued formatting my current code how I was familiar. 

## What I Learned

Explain what you learned by reviewing and applying the AI-assisted improvements.

I learned enumerate, which I began using in many other parts. Of course, I know the definition of the word, but I was not
initially aware of use here. I learned 'i' can be very helpful in many cases. During extra research to understand it, it
appears to be more advanced. Working through troubleshooting with AI generally revealed there are simpler ways to handle
the errors I was dealing with, even if it was longer lines of code. Overall, I learned a great deal during this project
and had fun getting into the zone (for 25-30hrs), adding additional functions to improve functionality each time the 
previous improvement was successful.