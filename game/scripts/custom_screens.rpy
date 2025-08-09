screen credits():
    tag menu

    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "credits"

        vbox:
            label "Artists"
            text _("- Loquacious Literature")
            text _("- migmonster1979")
            text _("- Iquano\n")

            label "Programmer"
            text _("- Myo Si Thu\n")

            ## gui.credits is usually set in options.rpy.
            if gui.credits:
                text "[gui.credits!t]\n"

            text _("Game source code available on {a=https://github.com/ozmandias/Harry-Potter-Book-Moments}GitHub{/a}.\n")


style credits_label is gui_label
style credits_label_text is gui_label_text
style credits_text is gui_text

style credits_label_text:
    size gui.label_text_size