#!/bin/bash
arecord --list-devices & cd AzureSpeechCC && /home/wordcloud/.dotnet/dotnet run & sleep 10s && sudo python3 write_to_screen.py

