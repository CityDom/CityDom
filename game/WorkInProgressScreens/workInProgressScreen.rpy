screen work_in_progress_screen():
    add workInProgress:
        at dissolve_transition
        xalign 0.5
        yalign 0.5
    timer 1.0 action Hide("work_in_progress_screen")

init python:
    def show_work_in_progress():
        renpy.show_screen("work_in_progress_screen")
