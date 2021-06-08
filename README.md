# Event Processing Pipeline

This repository contains a Event Processing Pipeline. It consists of two parts., in the first step all events are separated by event type. 

## Part I

`EventProcessingPartI` will received a file with all events and separate by event type and partition by the year, month and day of the date that the code was executed.

## Part II

In this part the code `EventProceeingPartII` will be triggered for each event type that were received in the first part and save in the output directory.


The `fake_events_generator.py` is used to generated fake events. Its receives the number of events to be generated and the output file.