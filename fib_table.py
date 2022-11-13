import re

initial_string = "#kdl_name = Fib_tab_buld\nApps.Fib.Table.Build : Apps.Fib.Table {\n  (Data.BaseTree.Bin.tie\n    (Data.BaseTree.Bin.tie\n      (Data.BaseTree.Bin.tie\n        Apps.Fib.Table.Build.gbin_00\n        Apps.Fib.Table.Build.gbin_01)\n      (Data.BaseTree.Bin.tie\n        Apps.Fib.Table.Build.gbin_02\n        Apps.Fib.Table.Build.gbin_03))\n    (Data.BaseTree.Bin.tie\n      (Data.BaseTree.Bin.tie\n        Apps.Fib.Table.Build.gbin_04\n        Apps.Fib.Table.Build.gbin_05)\n      (Data.BaseTree.Bin.tie\n        Apps.Fib.Table.Build.gbin_06\n        Apps.Fib.Table.Build.gbin_07))\n  )\n}\n#kdl_name = Fib_tab_pe\nApps.Fib.Table.Build.bin.empty_32 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2] U120 {\n  (Data.BaseTree.Bin.tie \n    Apps.Fib.Table.Build.bin.empty_16 \n    Apps.Fib.Table.Build.bin.empty_16\n  ) \n}\n\nApps.Fib.Table.Build.bin.empty_16 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2] U120 {\n  (Data.BaseTree.Bin.tie \n    Apps.Fib.Table.Build.bin.empty_8 \n    Apps.Fib.Table.Build.bin.empty_8\n  )\n}\n\nApps.Fib.Table.Build.bin.empty_8 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2] U120 {\n  (Data.BaseTree.Bin.tie \n    Apps.Fib.Table.Build.bin.empty_4 \n    Apps.Fib.Table.Build.bin.empty_4\n  ) \n}\n\nApps.Fib.Table.Build.bin.empty_4 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2] U120 {\n  (Data.BaseTree.Bin.tie \n    Apps.Fib.Table.Build.bin.empty_2 \n    Apps.Fib.Table.Build.bin.empty_2) \n}\n\nApps.Fib.Table.Build.bin.empty_2 : Data.BaseTree [Data.BaseTree.Base.2] U120 { \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))\n}\n\n#kdl_name = Fib_tab_gb00\nApps.Fib.Table.Build.gbin_00 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_00 Apps.Fib.Table.Build.bin_01)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_02 Apps.Fib.Table.Build.bin_03)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_04 Apps.Fib.Table.Build.bin_05)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_06 Apps.Fib.Table.Build.bin_07)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_08 Apps.Fib.Table.Build.bin_09)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_10 Apps.Fib.Table.Build.bin_11)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_12 Apps.Fib.Table.Build.bin_13)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_14 Apps.Fib.Table.Build.bin_15)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb01\nApps.Fib.Table.Build.gbin_01 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_16 Apps.Fib.Table.Build.bin_17)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_18 Apps.Fib.Table.Build.bin_19)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_20 Apps.Fib.Table.Build.bin_21)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_22 Apps.Fib.Table.Build.bin_23)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_24 Apps.Fib.Table.Build.bin_25)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_26 Apps.Fib.Table.Build.bin_27)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_28 Apps.Fib.Table.Build.bin_29)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_30 Apps.Fib.Table.Build.bin_31)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb02\nApps.Fib.Table.Build.gbin_02 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_32 Apps.Fib.Table.Build.bin_33)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_34 Apps.Fib.Table.Build.bin_35)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_36 Apps.Fib.Table.Build.bin_37)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_38 Apps.Fib.Table.Build.bin_39)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_40 Apps.Fib.Table.Build.bin_41)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_42 Apps.Fib.Table.Build.bin_43)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_44 Apps.Fib.Table.Build.bin_45)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_46 Apps.Fib.Table.Build.bin_47)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb03\nApps.Fib.Table.Build.gbin_03 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_48 Apps.Fib.Table.Build.bin_49)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_50 Apps.Fib.Table.Build.bin_51)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_52 Apps.Fib.Table.Build.bin_53)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_54 Apps.Fib.Table.Build.bin_55)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_56 Apps.Fib.Table.Build.bin_57)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_58 Apps.Fib.Table.Build.bin_59)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_60 Apps.Fib.Table.Build.bin_61)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_62 Apps.Fib.Table.Build.bin_63)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb04\nApps.Fib.Table.Build.gbin_04 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_64 Apps.Fib.Table.Build.bin_65)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_66 Apps.Fib.Table.Build.bin_67)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_68 Apps.Fib.Table.Build.bin_69)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_70 Apps.Fib.Table.Build.bin_71)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_72 Apps.Fib.Table.Build.bin_73)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_74 Apps.Fib.Table.Build.bin_75)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_76 Apps.Fib.Table.Build.bin_77)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_78 Apps.Fib.Table.Build.bin_79)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb05\nApps.Fib.Table.Build.gbin_05 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_80 Apps.Fib.Table.Build.bin_81)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_82 Apps.Fib.Table.Build.bin_83)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_84 Apps.Fib.Table.Build.bin_85)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_86 Apps.Fib.Table.Build.bin_87)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_88 Apps.Fib.Table.Build.bin_89)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_90 Apps.Fib.Table.Build.bin_91)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_92 Apps.Fib.Table.Build.bin_93)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_94 Apps.Fib.Table.Build.bin_95)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb06\nApps.Fib.Table.Build.gbin_06 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_96 Apps.Fib.Table.Build.bin_97)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_98 Apps.Fib.Table.Build.bin_99)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_100 Apps.Fib.Table.Build.bin_101)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_102 Apps.Fib.Table.Build.bin_103)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_104 Apps.Fib.Table.Build.bin_105)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_106 Apps.Fib.Table.Build.bin_107)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_108 Apps.Fib.Table.Build.bin_109)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_110 Apps.Fib.Table.Build.bin_111)\n      )\n    )\n  )   \n}\n#kdl_name = Fib_tab_gb07\nApps.Fib.Table.Build.gbin_07 : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 ] U120 {\n  (Data.BaseTree.Bin.tie \n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_112 Apps.Fib.Table.Build.bin_113)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_114 Apps.Fib.Table.Build.bin_115)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_116 Apps.Fib.Table.Build.bin_117)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_118 Apps.Fib.Table.Build.bin_119)\n      )\n    )\n    (Data.BaseTree.Bin.tie \n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_120 Apps.Fib.Table.Build.bin_121)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_122 Apps.Fib.Table.Build.bin_123)\n      )\n      (Data.BaseTree.Bin.tie \n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_124 Apps.Fib.Table.Build.bin_125)\n        (Data.BaseTree.Bin.tie Apps.Fib.Table.Build.bin_126 Apps.Fib.Table.Build.bin_127)\n      )\n    )\n  )}   \n\n"
stack = []
res = ''

file1 = open('tab.txt', 'r')
lines = file1.readlines()

lines = lines[0].replace('(D', '\n(D').split('\n')
i = 0
index = 0
while i < len(lines):
    if len(lines[i].split(' ')) <= 2:
        stack.append(lines[i])
        i += 1
    else:
        x = str(index).zfill(2)
        a = "#kdl_name = Fib_tab_p%s" % x + "\nApps.Fib.Table.Build.bin_%s : Data.BaseTree [Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2 Data.BaseTree.Base.2] U120 {" % x
        b = "}"
        res += a + '\n'
        for j in stack[-4:]:
            res += '  ' + j + '\n'
        for _ in range(27):
            res += '  ' + re.sub("[\)]{6,}", "))))))", lines[i]) + '\n'
            i += 1
        stack = []
        res += b + '\n'
        res += '\n'
        index += 1

branch_0 = "(Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))))))"
res = res.replace(branch_0, "Apps.Fib.Table.Build.bin.empty_32")
branch_1 = "(Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))) \n  (Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)))))"
res = res.replace(branch_1, "Apps.Fib.Table.Build.bin.empty_16")

branch_3 = "(Data.BaseTree.Bin.tie \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)) \n  (Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0)))"
res = res.replace(branch_3, "Apps.Fib.Table.Build.bin.empty_4")
branch_4 = "(Data.BaseTree.Bin.tie (U120.new 0 0) (U120.new 0 0))"
res = res.replace(branch_4, "Apps.Fib.Table.Build.bin.empty_2")
branch_2 = "(Data.BaseTree.Bin.tie \n  Apps.Fib.Table.Build.bin.empty_4 \n  Apps.Fib.Table.Build.bin.empty_4)"
res = res.replace(branch_2, "Apps.Fib.Table.Build.bin.empty_8")
f = open("Build_table.kind2", "w")
f.write(initial_string + res)
f.close()

