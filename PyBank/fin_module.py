#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Following is the function that holds the business logic of all core calculation for desired metrics
# This function takes a dictionary "budget_data" as argument with "date" as key and "pnl amount" as value in the dict and 
# return the required metrics in a python list

def calculate_fin_metrics(budget_data):
    # Initializations
    # we will use the variable "data_record_count" to store the total number of rows in the csv file (dataset)
    # Each rcord in the dataset represents a month. Hence at the end of file, final value of the vairbale  
    # "data_record_count" will give us the total number of months included in the 
    # dataset -> ANSWER TO THE FIRST QUESTION.

    # Initialize the variable "data_record_count" 

    data_record_count = 0

    # Initialize other metric variables
    total_pnl = 0;
    avg_change_in_pnl = 0;
    greatest_increase_in_profit = 0;
    greatest_decrease_in_losses = 0;

    # Initiatize other variables to facilitate intermediate computations
    previous_pnl_amount = 0
    current_pnl_amount = 0
    change = 0
    total_change = 0

    # Following are the processing logic:
    # (A) Iterate through each data-row in the dictionary "budget_data"
    # (B) Retrieve individual pnl amount of individual dictionary-row using date as the dictionary-key,
    #     convert retrieved pnl amount to integer and add to the 
    #     variable "total_pnl"=> ANSWER TO THE SECOND QUESTION

    for date_key in budget_data.keys():
        total_pnl = total_pnl + int(budget_data[date_key])

        # (C) To calculate the change in pnl amount, program has to remember immediate previous pnl amount and 
        #     subtract from current pnl amount
        #     (C.1) for the first row (data_record_count = 0) in the dictionary, 
        #           "current_pnl_amount" is set to the retrived value from dictionary
        #           previous_pnl_amount is not applicable for the fist row

        if data_record_count == 0:          # for first record
            current_pnl_amount = int(budget_data[date_key])

        #     (C.2) from second row onward, transfer "current_pnl-amount" to "previous_pnl_amount" and then
        #           "current_pnl_amount" will be set to retrieved value from dictionary

        else:                                # second record onward
            previous_pnl_amount = current_pnl_amount          # transfer current_pnl_amount to previous_pnl_amount 
            current_pnl_amount = int(budget_data[date_key])   # before it gets overeritten by retrived value
            change = current_pnl_amount - previous_pnl_amount # calculate the change at each iteration. 
                                                              # Calculation of change needs atleast 2 datapoints
                                                              # hence change is applicable from 2nd row onward
            total_change = total_change + change              # Capture individual change cummilatively 
                                                              # to total_change variable. 
                                                              # Dividing total_change by (data_record_count -1) 
                                                              # will gives us average change 
                                                              # => ANSWER TO THE THIRD QUESTION
                                                              # -1 in (data_record_count - 1) because changes are 
                                                              # calculated from second row onward

        # (D) Following "if block" checks if the record for profit, then computes greatest increase in profit 
        #     similarly "elif block" checks if the record for loss and the computes greatest decrease in losses 
        #     with their respective dates => ANSWER TO THE FOURTH AND FIFTH QUESTIONS

            if current_pnl_amount > 0:                           # check for profit
                if change > greatest_increase_in_profit:         # greatest_increase_in_profit variable is set to 
                    greatest_increase_in_profit = change         # the variable change, if change is greater
                    greatest_increase_in_profit_date = date_key  # save corresponding date for reporting

            elif current_pnl_amount < 0:                         # Check for loss
                if change < greatest_decrease_in_losses:         # greatest_decrease_in_losses variable is set to
                    greatest_decrease_in_losses = change         # the variable change, if change is lesser
                    greatest_decrease_in_losses_date = date_key  # save corresponding date for reporting

        # At the end of the processing of the current iteration increment data_record_count by +1

        data_record_count = data_record_count + 1

        # Control goes back to the for loop to repeat the code block  and this continues till 
        # end of the dictionary is reached

    ############################# OUTSIDE OF FOR LOOP #################################

    avg_change_in_pnl = round(total_change / (data_record_count -1),2)
    
    
    # Construct the list of all calculated metrics and the return the list to the caller
    
    metrics = [data_record_count,total_pnl,avg_change_in_pnl,greatest_increase_in_profit_date,
               greatest_increase_in_profit,greatest_decrease_in_losses_date,greatest_decrease_in_losses]
    
    return metrics
    
    ############################ END OF FUNCTION ########################################

