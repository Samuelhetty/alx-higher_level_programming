#!/bin/bash
# POST request with curl and --data params to input URL
curl -s --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
