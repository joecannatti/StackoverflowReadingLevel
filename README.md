
This project computes the Flesch-Kincaid grade level for each tag on stackoverflow
---


Copy Posts.xml from the stackoverflow dump into the data directory

Run `src/split_posts_xml_file.sh`

Run `src/process_xml.sh`, wait for all 8 process to finish, run `tail_processes.sh` to view progress

Run `src/append_files.sh`

Run `python src/denormalize_parent_tags.py`

Run `python src/split_rows_by_tag.py`

Run src/chart_reading_levels.py from an ipython session

