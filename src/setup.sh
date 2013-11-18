git clone https://github.com/wimmuskee/readability-score.git
sudo apt-get install python-yaml
sudo pip install nltk
sudo pip install hyphenator
sudo apt-get install myspell-en-us
sudo cp /usr/share/myspell/dicts/hyph_en_US.dic /usr/share/myspell/
cd readability-score; sudo python setup.py install
sudo pip install beautifulsoup4
