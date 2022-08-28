#!/usr/bin/env python
# coding: utf-8

# In[2]:


import ezgmail


# In[3]:


def attachmentdownload(resulthreads):
    #two objects used in code are GmailThread and GmailMessage
    #1. GmailThread - Represents conversation threads
    #2. GmailMessage - Represents individual emails within Threads
    countofresults = len(resulthreads)
    try:
        for i in range(countofresult):
            #checks whether the count of messages in threads is greaer than 1
            if len(resulthreads[i].messages)> 1:
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[j].downloadallAttachments()
            else:
                #downloads attachment(s) for single message 
                resulthreads[i].messages[j].downloadAllAttachments()
        print("Download complete. Please check your root directory.")
    except:
        raise Exception("Error occured while downloading attachment(s).")


    
    


# In[5]:


if __name__ =='__main__':
    query = input("Enter search query: ")
    #appending to make sure the result threads always has an attachment
    newquery = query + "+ has:attachment"
    # search functions accepts all the operators 
    resultthreads = ezgmail.search(newquery)
    
    if len(resultthreads) == 0:
       #executed if results don't have attachment
       print("Result has no attachments:")
    else:
        print("Result(s) with attachments:")
        for threads in resulthreads:
            #prints the subject line of email thread in results
            print(f"Email Subject: {threads.messages[0].subject}" )
        try:
            ask = input(
                 "Do you want to download attachment(s) in result(s) (Yes/No)?")
            if ask == "Yes":
                # calls the function that downloads attachment(s)
                attachmentdownload(resulthreads)
            else:
                print("Program exited")
        except:
            print("Something went wrong")
    


# In[ ]:




