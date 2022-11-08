#############################################################################
# Generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#  Nov 07, 2022 07:31:11 PM PST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #d9d9d9
set vTcl(actual_gui_menu_analog) #d9d9d9
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m47" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1020x691+363+124
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1041
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Regression Explorer"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "MainWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu $top.m47 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $top.m47 add command \
        -command {#import_window} -label Import... -state normal 
    
set site_3_0 $top.m47
    $top.m47 add cascade \
        -menu "$top.m47.men49" -command {{}} -label DataFrame -state normal 
    menu $site_3_0.men49 \
        -activebackground beige -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men49 add command \
        -command {#menu_df_info} -label Info 
    $site_3_0.men49 add command \
        -command {#menu_df_describe} -label Describe 
    $site_3_0.men49 add command \
        -command {#menu_df_dropna} -label {Drop NA} 
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list selected $vTcl(actual_gui_bg) active $vTcl(tabbg1) !active $vTcl(tabbg2)]
    ttk::style map TNotebook.Tab -foreground [list selected $vTcl(actual_gui_fg) active $vTcl(tabfg1) !active $vTcl(tabfg2)]
    ttk::notebook $top.tNo46 \
        -width 1021 -height 716 -takefocus {} 
    vTcl:DefineAlias "$top.tNo46" "TabGroup" vTcl:WidgetProc "MainWindow" 1
    frame $top.tNo46.t0 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo46.t0" "PairPlotTab" vTcl:WidgetProc "MainWindow" 1
    $top.tNo46 add $top.tNo46.t0 \
        -padding 0 -sticky nsew -state normal -text EDA -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo46.t0
    frame $site_4_0.fra47 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 676 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 729 
    vTcl:DefineAlias "$site_4_0.fra47" "PairPlotFrame" vTcl:WidgetProc "MainWindow" 1
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $site_4_0.tPa55
    vTcl:DefineAlias "$site_4_0.tPa55" "LeftPaneGroup" vTcl:WidgetProc "MainWindow" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa55.p1 \
        -text {PairPlot Option} -width 200 -height 45 
    vTcl:DefineAlias "$site_4_0.tPa55.p1" "PlotOptionsPane" vTcl:WidgetProc "MainWindow" 1
    set site_6_0 $site_4_0.tPa55.p1
    ttk::combobox $site_6_0.tCo60 \
        \
        -values {linear {log base 10} {natural log} {square root} categorical exclude index} \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_6_0.tCo60" "PlotOptionMenu" vTcl:WidgetProc "MainWindow" 1
    bind $site_6_0.tCo60 <<ComboboxSelected>> {
        plot_option_changed
    }
    place $site_6_0.tCo60 \
        -in $site_6_0 -x 0 -y 0 -rely 0.444 -width 0 -relwidth 1 -height 0 \
        -relheight 0.467 -anchor nw -bordermode ignore 
    $site_4_0.tPa55 add $site_4_0.tPa55.p1 
    $site_4_0.tPa55 pane $site_4_0.tPa55.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tPa55.p2 \
        -width 200 -height 125 
    vTcl:DefineAlias "$site_4_0.tPa55.p2" "HeaderPane" vTcl:WidgetProc "MainWindow" 1
    set site_6_1 $site_4_0.tPa55.p2
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $site_6_1.scr56 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_6_1.scr56" "HeaderList" vTcl:WidgetProc "MainWindow" 1
    bind $site_6_1.scr56 <<ListboxSelect>> {
        header_select
    }

    $site_6_1.scr56.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -listvariable header_list
    place $site_6_1.scr56 \
        -in $site_6_1 -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    $site_4_0.tPa55 add $site_4_0.tPa55.p2 
    $site_4_0.tPa55 pane $site_4_0.tPa55.p2 -weight 0
$site_6_0 configure -height 45
    vTcl:copy_lock $site_4_0.tPa55
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu46 \
        -command create_pairplot -takefocus {} -text PairPlot -compound left 
    vTcl:DefineAlias "$site_4_0.tBu46" "PairPlotButton" vTcl:WidgetProc "MainWindow" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_4_0.tBu47 \
        -command create_clustermap -takefocus {} -text ClusterMap \
        -compound left 
    vTcl:DefineAlias "$site_4_0.tBu47" "ClusterMapButton" vTcl:WidgetProc "MainWindow" 1
    place $site_4_0.fra47 \
        -in $site_4_0 -x 0 -relx 0.285 -y 0 -width 0 -relwidth 0.717 \
        -height 0 -relheight 1.003 -anchor nw -bordermode ignore 
    place $site_4_0.tPa55 \
        -in $site_4_0 -x 0 -relx 0.029 -y 0 -rely 0.043 -width 0 \
        -relwidth 0.226 -height 0 -relheight 0.877 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tBu46 \
        -in $site_4_0 -x 0 -relx 0.049 -y 0 -rely 0.933 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tBu47 \
        -in $site_4_0 -x 0 -relx 0.138 -y 0 -rely 0.933 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    frame $top.tNo46.t1 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo46.t1" "RegressionTab" vTcl:WidgetProc "MainWindow" 1
    $top.tNo46 add $top.tNo46.t1 \
        -padding 0 -sticky nsew -state normal -text Regression -image {} \
        -compound left -underline -1 
    set site_4_1  $top.tNo46.t1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.001 -height 0 \
        -relheight 0.999 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top2 {base} {
    global vTcl
    if {$base == ""} {
        set base .top2
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 533x193+716+235
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Import File"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "ImportWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    ttk::entry $top.tEn63 \
        -font TkTextFont -textvariable input_file_str -validate focusout \
        -validatecommand {validate_input_file %P} -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$top.tEn63" "InputFileField" vTcl:WidgetProc "ImportWindow" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu64 \
        -command open_file_chooser -takefocus {} -text Select -compound left 
    vTcl:DefineAlias "$top.tBu64" "SelectFileButton" vTcl:WidgetProc "ImportWindow" 1
    ttk::entry $top.tEn65 \
        -font TkTextFont -textvariable import_kwargs_str -validate focusout \
        -validatecommand {validate_import_kwargs %P} -foreground {} \
        -background {} -takefocus {} -cursor ibeam 
    vTcl:DefineAlias "$top.tEn65" "ImportKwargsField" vTcl:WidgetProc "ImportWindow" 1
    ttk::label $top.tLa66 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {Input File:} -compound left 
    vTcl:DefineAlias "$top.tLa66" "ImportFileLabel" vTcl:WidgetProc "ImportWindow" 1
    ttk::label $top.tLa67 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {Import kwargs:} -compound left 
    vTcl:DefineAlias "$top.tLa67" "ImportKwargsLabel" vTcl:WidgetProc "ImportWindow" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu68 \
        -command import_file -takefocus {} -text Import -compound left \
        -state disabled 
    vTcl:DefineAlias "$top.tBu68" "ImportButton" vTcl:WidgetProc "ImportWindow" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu69 \
        -command import_cancel -takefocus {} -text Cancel -compound left 
    vTcl:DefineAlias "$top.tBu69" "CancelButton" vTcl:WidgetProc "ImportWindow" 1
    menu $top.m46 \
        -activebackground #ececec -activeforeground #000000 \
        -background $vTcl(actual_gui_menu_bg) -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tEn63 \
        -in $top -x 0 -relx 0.056 -y 0 -rely 0.207 -width 376 -relwidth 0 \
        -height 21 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tBu64 \
        -in $top -x 0 -relx 0.788 -y 0 -rely 0.207 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tEn65 \
        -in $top -x 0 -relx 0.056 -y 0 -rely 0.518 -width 466 -relwidth 0 \
        -height 21 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tLa66 \
        -in $top -x 0 -relx 0.056 -y 0 -rely 0.052 -width 0 -relwidth 0.109 \
        -height 0 -relheight 0.124 -anchor nw -bordermode ignore 
    place $top.tLa67 \
        -in $top -x 0 -relx 0.056 -y 0 -rely 0.363 -width 0 -relwidth 0.158 \
        -height 0 -relheight 0.124 -anchor nw -bordermode ignore 
    place $top.tBu68 \
        -in $top -x 0 -relx 0.356 -y 0 -rely 0.725 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tBu69 \
        -in $top -x 0 -relx 0.507 -y 0 -rely 0.725 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top3 {base} {
    global vTcl
    if {$base == ""} {
        set base .top3
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x233+655+310
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4484 2326
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "DataFrame Descrption"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "DescDialog" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu46 \
        -command close_desc -takefocus {} -text Close -compound left 
    vTcl:DefineAlias "$top.tBu46" "DescCloseButton" vTcl:WidgetProc "DescDialog" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr46" "DescTextBox" vTcl:WidgetProc "DescDialog" 1

    $top.scr46.01 configure -background #ffffff \
        -font "-family {Courier New} -size 11" \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -relief flat \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -state disabled \
        -width 10 \
        -wrap none
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tBu46 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.871 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $top.scr46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 0.849 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top4 {base} {
    global vTcl
    if {$base == ""} {
        set base .top4
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 404x450+593+474
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4484 2326
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "DataFrame Info"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "InfoDialog" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu46 \
        -command close_info -takefocus {} -text Close -compound left 
    vTcl:DefineAlias "$top.tBu46" "InfoCloseButton" vTcl:WidgetProc "InfoDialog" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr48 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr48" "InfoTextBox" vTcl:WidgetProc "InfoDialog" 1

    $top.scr48.01 configure -background #ffffff \
        -font "-family {Courier New} -size 11" \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -relief flat \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -state disabled \
        -width 10 \
        -wrap none
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tBu46 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.92 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $top.scr48 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 0.9 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top5 {base} {
    global vTcl
    if {$base == ""} {
        set base .top5
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 822x607+531+125
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    set toptitle "Drop NA Values"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "DnaDialog" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr48 \
        -borderwidth 2 -relief groove -width 125 -height 113 
    vTcl:DefineAlias "$top.tFr48" "DnaAxisFrame" vTcl:WidgetProc "DnaDialog" 1
    set site_3_0 $top.tFr48
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $site_3_0.tRa49 \
        -variable dropna_axis -text Columns* -compound left 
    vTcl:DefineAlias "$site_3_0.tRa49" "DnaAxisRadio2" vTcl:WidgetProc "DnaDialog" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $site_3_0.tRa50 \
        -variable dropna_axis -value 0 -text Rows -compound left 
    vTcl:DefineAlias "$site_3_0.tRa50" "DnaAxisRadio1" vTcl:WidgetProc "DnaDialog" 1
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text {Axis to remove:} \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa51" "DnaAxisLabel" vTcl:WidgetProc "DnaDialog" 1
    place $site_3_0.tRa49 \
        -in $site_3_0 -x 0 -relx 0.08 -y 0 -rely 0.531 -width 0 \
        -relwidth 0.832 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tRa50 \
        -in $site_3_0 -x 0 -relx 0.082 -y 0 -rely 0.336 -width 0 \
        -relwidth 0.842 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 0 -relx 0.08 -y 0 -rely 0.08 -width 0 -relwidth 0.84 \
        -height 0 -relheight 0.239 -anchor nw -bordermode ignore 
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr46 \
        -borderwidth 2 -relief groove -width 145 -height 116 
    vTcl:DefineAlias "$top.tFr46" "DnaHowFrame" vTcl:WidgetProc "DnaDialog" 1
    set site_3_0 $top.tFr46
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $site_3_0.tRa48 \
        -variable dropna_how -text Any -compound left 
    vTcl:DefineAlias "$site_3_0.tRa48" "DnaHowRadio1" vTcl:WidgetProc "DnaDialog" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $site_3_0.tRa49 \
        -variable dropna_how -value 2 -text All -compound left 
    vTcl:DefineAlias "$site_3_0.tRa49" "DnaHowRadio2" vTcl:WidgetProc "DnaDialog" 1
    ttk::style configure TRadiobutton -background $vTcl(actual_gui_bg)
    ttk::style configure TRadiobutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TRadiobutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::radiobutton $site_3_0.tRa50 \
        -variable dropna_how -value 3 -text {At least} -compound left 
    vTcl:DefineAlias "$site_3_0.tRa50" "DnaHowRadio3" vTcl:WidgetProc "DnaDialog" 1
    ttk::label $site_3_0.tLa51 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text {NaNs required:} \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa51" "DnaHowLabel" vTcl:WidgetProc "DnaDialog" 1
    spinbox $site_3_0.spi52 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 2.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -to 100.0 
    vTcl:DefineAlias "$site_3_0.spi52" "DnaMinNA" vTcl:WidgetProc "DnaDialog" 1
    place $site_3_0.tRa48 \
        -in $site_3_0 -x 0 -relx 0.07 -y 0 -rely 0.354 -width 0 \
        -relwidth 0.834 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tRa49 \
        -in $site_3_0 -x 0 -relx 0.07 -y 0 -rely 0.54 -width 0 \
        -relwidth 0.834 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tRa50 \
        -in $site_3_0 -x 0 -relx 0.07 -y 0 -rely 0.726 -width 0 \
        -relwidth 0.834 -height 0 -relheight 0.186 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa51 \
        -in $site_3_0 -x 0 -relx 0.069 -y 0 -rely 0.088 -width 0 \
        -relwidth 0.862 -height 0 -relheight 0.239 -anchor nw \
        -bordermode ignore 
    place $site_3_0.spi52 \
        -in $site_3_0 -x 0 -relx 0.552 -y 0 -rely 0.726 -width 0 \
        -relwidth 0.372 -height 0 -relheight 0.168 -anchor nw \
        -bordermode ignore 
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr53 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr53" "DnaCurrentTextBox" vTcl:WidgetProc "DnaDialog" 1

    $top.scr53.01 configure -background white \
        -font "-family {Courier New} -size 11" \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr54 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr54" "DnaAfterTextBox" vTcl:WidgetProc "DnaDialog" 1

    $top.scr54.01 configure -background white \
        -font "-family {Courier New} -size 11" \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame $top.tFr47 \
        -borderwidth 2 -relief groove -width 111 -height 113 
    vTcl:DefineAlias "$top.tFr47" "DnaButtonFrame" vTcl:WidgetProc "DnaDialog" 1
    set site_3_0 $top.tFr47
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu46 \
        -command dna_dropna('apply') -takefocus {} -text Apply -compound left 
    vTcl:DefineAlias "$site_3_0.tBu46" "DnaApplyButton" vTcl:WidgetProc "DnaDialog" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu47 \
        -command dna_dropna('commit') -takefocus {} -text Commit \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tBu47" "DnaCommitButton" vTcl:WidgetProc "DnaDialog" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu48 \
        -command close_dropna -takefocus {} -text Close -compound left 
    vTcl:DefineAlias "$site_3_0.tBu48" "DnaCloseButton" vTcl:WidgetProc "DnaDialog" 1
    place $site_3_0.tBu46 \
        -in $site_3_0 -x 0 -relx 0.18 -y 0 -rely 0.115 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu47 \
        -in $site_3_0 -x 0 -relx 0.18 -y 0 -rely 0.398 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu48 \
        -in $site_3_0 -x 0 -relx 0.18 -y 0 -rely 0.681 -width 76 -relwidth 0 \
        -height 25 -relheight 0 -anchor nw -bordermode ignore 
    ttk::label $top.tLa49 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text Current -compound left 
    vTcl:DefineAlias "$top.tLa49" "DnaCurrentLabel" vTcl:WidgetProc "DnaDialog" 1
    ttk::label $top.tLa50 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text {After Drop NA} \
        -compound left 
    vTcl:DefineAlias "$top.tLa50" "DnaAfterLabel" vTcl:WidgetProc "DnaDialog" 1
    ttk::label $top.tLa47 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left \
        -text {*Removing columns will reset EDA plot settings} -compound left 
    vTcl:DefineAlias "$top.tLa47" "DnaColumnsNote" vTcl:WidgetProc "DnaDialog" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tFr48 \
        -in $top -x 0 -relx 0.012 -y 0 -rely 0.016 -width 0 -relwidth 0.208 \
        -height 0 -relheight 0.186 -anchor nw -bordermode ignore 
    place $top.tFr46 \
        -in $top -x 0 -relx 0.231 -y 0 -rely 0.016 -width 0 -relwidth 0.242 \
        -height 0 -relheight 0.186 -anchor nw -bordermode ignore 
    place $top.scr53 \
        -in $top -x 0 -y 0 -rely 0.297 -width 0 -relwidth 0.501 -height 0 \
        -relheight 0.705 -anchor nw -bordermode ignore 
    place $top.scr54 \
        -in $top -x 0 -relx 0.499 -y 0 -rely 0.297 -width 0 -relwidth 0.5 \
        -height 0 -relheight 0.705 -anchor nw -bordermode ignore 
    place $top.tFr47 \
        -in $top -x 0 -relx 0.487 -y 0 -rely 0.016 -width 0 -relwidth 0.135 \
        -height 0 -relheight 0.186 -anchor nw -bordermode ignore 
    place $top.tLa49 \
        -in $top -x 0 -y 0 -rely 0.247 -width 0 -relwidth 0.491 -height 0 \
        -relheight 0.048 -anchor nw -bordermode ignore 
    place $top.tLa50 \
        -in $top -x 0 -relx 0.499 -y 0 -rely 0.247 -width 0 -relwidth 0.493 \
        -height 0 -relheight 0.048 -anchor nw -bordermode ignore 
    place $top.tLa47 \
        -in $top -x 0 -relx 0.012 -y 0 -rely 0.214 -width 0 -relwidth 0.493 \
        -height 0 -relheight 0.031 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}
proc validate_import_kwargs {args} {return 1}
proc validate_input_file {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top2 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}
set btop3 ""
if {$vTcl(borrow)} {
    set btop3 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop3 $vTcl(tops)] != -1} {
        set btop3 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop3
Window show .top3 $btop3
if {$vTcl(borrow)} {
    $btop3 configure -background plum
}
set btop4 ""
if {$vTcl(borrow)} {
    set btop4 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop4 $vTcl(tops)] != -1} {
        set btop4 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop4
Window show .top4 $btop4
if {$vTcl(borrow)} {
    $btop4 configure -background plum
}
set btop5 ""
if {$vTcl(borrow)} {
    set btop5 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop5 $vTcl(tops)] != -1} {
        set btop5 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop5
Window show .top5 $btop5
if {$vTcl(borrow)} {
    $btop5 configure -background plum
}

