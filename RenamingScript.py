
import os
os.chdir("/home/stanislav/PycharmProjects/untitled/MatPhagAltAppr")
#dir = '/home/stanislav/PycharmProjects/untitled/Data_8362/2016-03-29_mb_8362_APPPS1_ATP_2002_repr_2_nonsplit300_Statistics'
#excessive = '2016-03-29_mb_8362_APPPS1_ATP_2002_repr_2_nonsplit300_'
#excessive2 = '2016-03-29_mb_8362_APPPS1_ATP_2002_repr_2_2016-03-29_mb_8362_APPPS1_ATP_2002_repr_nonsplit300_'
for folder in os.listdir("."):
    os.chdir("/home/stanislav/PycharmProjects/untitled/MatPhagAltAppr/%s" % folder)
    for data_folder in os.listdir("."):
        os.chdir("/home/stanislav/PycharmProjects/untitled/MatPhagAltAppr/%s/%s" % (folder, data_folder))
        excessive = data_folder.split("Statistics")[0]
        for filename in os.listdir("."):
            path = os.path.join("/home/stanislav/PycharmProjects/untitled/MatPhagAltAppr/%s/%s" % (folder, data_folder), filename)
            target = os.path.join("/home/stanislav/PycharmProjects/untitled/MatPhagAltAppr/%s/%s" % (folder, data_folder), filename.replace(excessive, ''))
            os.rename(path, target)

    # for filename in os.listdir(dir):
    #     path = os.path.join(dir, filename)
    #     target = os.path.join(dir, filename.replace(excessive2, ''))
    #     os.rename(path, target)

# import os
# import shutil
#
# os.chdir("/home/stanislav/Shu-Farn/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18_20180928_111341/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18")
# #dir = '/home/stanislav/PycharmProjects/untitled/Data_8362/2016-03-29_mb_8362_APPPS1_ATP_2002_repr_2_nonsplit300_Statistics'
# for file in os.listdir("."):
#     if len(file)>80:
#         excessive = file[:-28]
#         ending = file[-29:]
#         directory = os.path.join("/home/stanislav/Shu-Farn/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18_20180928_111341/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18/%s" % excessive)
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#         path = os.path.join("/home/stanislav/Shu-Farn/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18_20180928_111341/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18/%s" % file)
#         target = os.path.join("/home/stanislav/Shu-Farn/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18_20180928_111341/GAH cyfip primary microglia 2-2 Phrodo- shu farn 28.9.18/%s/%s" % (excessive, ending))
#         if (os.path.isfile(path)):
#             shutil.move(path, target)
#
#     #os.rename(copy_file, target)
#
#     # for filename in os.listdir(dir):
#     #     path = os.path.join(dir, filename)
#     #     target = os.path.join(dir, filename.replace(excessive2, ''))
#     #     os.rename(path, target)
