# FB Arhive Browser

A utility for browsing your Facebook archive.


## Features in development

- [x] Browse conversations list
- [ ] Load conversations
- [ ] Advanced message search


## Dependencies

- PyQt5


## Usage

1.  Download your information from Facebook
    1.  Visit https://www.facebook.com/settings?tab=your_facebook_information
    2.  Select "Download your information"
    3.  "New file" -> "Format: JSON" (select other options as desired) -> "Create file"
    4.  Wait for your information archive to be generated and download when ready.

2.  Unzip the archive downloaded from Facebook and place the unzipped folder into the `data` directory

3.  Run the program by launching `main.py` with Python 3


### How can I trust this software with my Facebook data?

This program is written in Python and is published as open-source, meaning that there is no pre-compiled or obfuscated code running when you launch it.

All of the code that makes up this program is freely available in the `src` folder of this repository. You may verify that there is no networking code, meaning that your Facebook data will not be sent to other computers or the internet.


### License

This software is published under the GPLv3 license. See the [LICENSE](LICENSE) file for more information.
