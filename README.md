# Template for EPL's UCLouvain Ph.D. Theses

This repository contains a template to write your thesis with the CIACO's requirements.
Just look at either thesis_a4.tex or thesis_elec.tex and start writing :-)

NB: For the bibliography, use Biber instead of BibTex.

## Thesis format

Two main files are proposed: either writing on A4 format (thesis_a4.tex) or on the CIACO specific one (thesis_elec.tex).
Both formats should work for the CIACO, but make sure you mention the format you use when sending your PDF for printing!

## Continuous Integration with GitHub

If you use GitHub to host your repository, you can leverage the GitHub Actions to auto-generate the thesis PDF.
For this, you have a few environment variables to configure this workflow:

| env variable  | purpose   |
|---|---|
| **MAIN_LATEX**  | The entry point of your thesis (here it is thesis_elec.tex)  |
| **FINAL_FILENAME**   | The final name of the file, which follows the naming conventions of the UCLouvain (for example :  Yakoub_13861700_2020.pdf )   |
| **DATE_TIMEZONE**  | The timezone for release (by default, Github uses GMT timezone)  |

Then in the Actions tab of your GitHub repository, you can build the thesis.

# CIACO specific info regarding thesis printing

Detailed considerations are available on [Ciaco's website](https://www.ciaco.coop/imprimerie/theses-trucs-astuces)

## Finding colored pages

The python script `find_color_pages.py` will detect pages to be printed in color.
CIACO will ask for those pages when printing the manuscript.

The script is configured to parse the `thesis_elec.pdf`, be sure to modify the variable `thesis_file` if another pdf must be read.

Thanks to Maxime Piraux for providing the original parsing script.

## Cover information

CIACO will ask you for a small file (.txt or word) containing the following data:

- title
- (potential sub-title)
- abbreviated title for the spine of the thesis (max 80 char., including space)
- name and firstname
- full coordinates (faculty, department, unit, adress, phone, fac, mail, website)
- date
- short abstract and biography (max 2000 char., including space)
- collection number

A sample file is provided in `cover_info.txt`

Please refer for their website for more complete informations if needed.
