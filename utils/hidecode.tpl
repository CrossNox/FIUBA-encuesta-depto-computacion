((*- extends 'latex/report.tex.j2' -*))

((*- block margins -*))
    \geometry{verbose,tmargin=.5in,bmargin=.7in,lmargin=.5in,rmargin=.5in}
((*- endblock margins -*))

((* block input_group *))
    ((*- if cell.metadata.get('nbconvert', {}).get('show_code', False) -*))
        ((( super() )))
    ((*- endif -*))
((* endblock input_group *))

((* block stream *))
((* endblock stream *))

((* block execute_result *))
((( super() )))
((* endblock execute_result *))

((* block display_data *))
((( super() )))
((* endblock display_data *))

