#!/usr/bin/node

const argc = process.argv

if (argc < 2) {
    console.log('No arguments')
} else if (argc === 2) {
    console.log(argc[2])
}