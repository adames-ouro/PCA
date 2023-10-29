# Libraries
try: 
    import pandas as pd
except:
    print("Install pandas")

try:
    import pandas.api.types as ptypes
except:
    print("Install pandas.api.types")

try:
    import matplotlib.pyplot as plt
except:
    print("Install matplotlib")

try:
    from matplotlib.cm import get_cmap
except:
    print("Install matplotlib.cm ")

    
def vars_samples_plot(ProjectedData:pd.DataFrame,Loadings:pd.DataFrame,ExplainedVar:list,**kwargs):

    # Optional arguments
    Fig_size = kwargs.get('Fig_size', (16, 12))
    Fig_size_sub = kwargs.get('Fig_size', (20, 12))
    Overlaid = kwargs.get('Overlaid', True)
    Plot_style = kwargs.get('Plot_style', 'classic')
    Color_by_disc_var = kwargs.get('Color_by_disc_var', None)
    Sample_colors = kwargs.get('Sample_colors','blue')
    Sample_size = kwargs.get('Sample_size',15)
    Sample_labels = kwargs.get('Sample_labels',True)
    Sample_labels_color = kwargs.get('Sample_labels_color','black')
    Sample_labels_size = kwargs.get('Sample_labels_size',10)
    Sample_labels_shift = kwargs.get('Sample_labels_shift',.02)
    Arrow_colors = kwargs.get('Arrow_colors','red')
    Arrow_head_size = kwargs.get('Arrow_head_size',0.05)
    Arrow_labels = kwargs.get('Arrow_labels',True)
    Arrow_labels_size = kwargs.get('Arrow_labels_size',10)
    Arrow_labels_color = kwargs.get('Arrow_labels_color','black')
    Arrow_labels_shift = kwargs.get('Arrow_labels_shift',1.15)
    X_label_size = kwargs.get('X_label_size',15)
    Y_label_size = kwargs.get('Y_label_size',15)
    Title_size = kwargs.get('Title_size',20)
    
    # Assertions
    assert type(ProjectedData) == pd.DataFrame, "The argument ProjectedData in this function must be a data frame. You passed a " + str(type(ProjectedData))

    assert type(Loadings) == pd.DataFrame, "The argument Loadings in this function must be a data frame. You passed a " + str(type(Loadings))

    assert all(ptypes.is_numeric_dtype(ProjectedData[col]) for col in ProjectedData.columns) , "ProjectedData must be an all numeric data frame"

    assert all(ptypes.is_numeric_dtype(Loadings[col]) for col in Loadings.columns) , "Loadings must be an all numeric data frame"

    assert type(ExplainedVar) == list, "The argument ExplainedVar in this function is a list. You passed a " + str(type(ExplainedVar))

    assert all(type(item)!=str for item in ExplainedVar), "The list for ExplainedVar must contains numbers"
  
    plt.style.use(Plot_style)
    
    if Color_by_disc_var is None:

        # Condition for 1 or 2 plots
        if Overlaid == True:
            # figure size
            fig = plt.figure(figsize=Fig_size)
            ax = fig.add_subplot()

            # labels and title
            ax.set_xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            ax.set_ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            ax.set_title('2 Components', fontsize = Title_size)
            ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)

            # plot
            row_list=[]

            for i in range(0,len(ProjectedData)):
                row_list.append(list(ProjectedData.index)[i])
                row_list.append(i)
        
            row = iter(row_list)
            row_dct = dict(zip(row, row))

            # sample labels 
            if Sample_labels == True:
                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)
                    plt.text(x+Sample_labels_shift, y+Sample_labels_shift, row_word, fontsize=Sample_labels_size, color = Sample_labels_color)
            else:
                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)
            
            # loading labels
            if Arrow_labels == True:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
                    plt.text(Loadings.iloc[i,0]* Arrow_labels_shift, Loadings.iloc[i,1] * Arrow_labels_shift, Loadings.index[i], color=Arrow_labels_color, fontsize = Arrow_labels_size, ha='center', va='center')
            else:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
        else:
            # subplots to divide plot
            plt.figure(figsize=Fig_size_sub)
            plt.subplot(1, 2, 1)

            # plot of projected data
            row_list=[]

            for i in range(0,len(ProjectedData)):
                row_list.append(list(ProjectedData.index)[i])
                row_list.append(i)
        
            row = iter(row_list)
            row_dct = dict(zip(row, row))

            if Sample_labels == True:
                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)
                    plt.text(x+Sample_labels_shift, y+Sample_labels_shift, row_word, fontsize=Sample_labels_size, color = Sample_labels_color)
            else:
                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)

            plt.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            plt.ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            plt.title('2 Components - Observations', fontsize = Title_size)

            # plot of loadings
            plt.subplot(1, 2, 2)

            if Arrow_labels == True:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
                    plt.text(Loadings.iloc[i,0]* (Arrow_labels_shift -.1), Loadings.iloc[i,1] * (Arrow_labels_shift -.1), Loadings.index[i], color=Arrow_labels_color, fontsize = Arrow_labels_size, ha='center', va='center')
            else:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)

            plt.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            plt.ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            plt.title('2 Components - Variable Characterization', fontsize = Title_size)

    else:
        name1 = "tab10"
        cmap1 = get_cmap(name1)
        colors_list1 = cmap1.colors

        name2 = 'Set3'
        cmap2 = get_cmap(name2)
        colors_list2 = cmap2.colors

        color_list=[]

        for i in colors_list1:
            color_list.append(i)

        for i in colors_list2:
            color_list.append(i)

        targets = Color_by_disc_var.iloc[:,0].unique()
        colors = color_list[0:len(targets)]

        # Condition for 1 or 2 plots
        if Overlaid == True:
            # figure size
            fig = plt.figure(figsize=Fig_size)
            ax = fig.add_subplot()

            # labels and title
            ax.set_xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            ax.set_ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            ax.set_title('2 Components', fontsize = Title_size)
            ax.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            ax.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)

            # plot
            row_list=[]

            for i in range(0,len(ProjectedData)):
                row_list.append(list(ProjectedData.index)[i])
                row_list.append(i)
        
            row = iter(row_list)
            row_dct = dict(zip(row, row))

            #color based on variable
            color=[]
            for i in targets:
                color.append(colors[i])

            # sample labels 
            if Sample_labels == True:
                for target, color in zip(targets,colors):
                    indicesToKeep = Color_by_disc_var == target
                    ax.scatter(ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[0]],ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[1]], marker='o', color=color, s = 15,label='samples')

                L=plt.legend()
                for l in targets:
                    L.get_texts()[l].set_text(targets[l])
                    

                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    #plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)
                    plt.text(x+Sample_labels_shift, y+Sample_labels_shift, row_word, fontsize=Sample_labels_size, color = Sample_labels_color)
            else:
                for target, color in zip(targets,colors):
                    indicesToKeep = Color_by_disc_var == target
                    ax.scatter(ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[0]],ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[1]], marker='o', color=color, s = 15,label='samples')
                
                L=plt.legend()
                for l in targets:
                    L.get_texts()[l].set_text(targets[l])

            # loading labels
            if Arrow_labels == True:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
                    plt.text(Loadings.iloc[i,0]* Arrow_labels_shift, Loadings.iloc[i,1] * Arrow_labels_shift, Loadings.index[i], color=Arrow_labels_color, fontsize = Arrow_labels_size, ha='center', va='center')
            else:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
        else:
            # subplots to divide plot
            plt.figure(figsize=Fig_size_sub)
            plt.subplot(1, 2, 1)

            # plot of projected data
            row_list=[]

            for i in range(0,len(ProjectedData)):
                row_list.append(list(ProjectedData.index)[i])
                row_list.append(i)
        
            row = iter(row_list)
            row_dct = dict(zip(row, row))

                        #color based on variable
            color=[]
            for i in targets:
                color.append(colors[i])

            if Sample_labels == True:
                for target, color in zip(targets,colors):
                    indicesToKeep = Color_by_disc_var == target
                    plt.scatter(ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[0]],ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[1]], marker='o', color=color, s = 15)

                for row_word in list(ProjectedData.index):
                    x, y =ProjectedData.iloc[[row_dct[row_word]],[0,1]].values[0]
                    #plt.scatter(x, y, marker='o', color=Sample_colors, s = Sample_size)
                    plt.text(x+Sample_labels_shift, y+Sample_labels_shift, row_word, fontsize=Sample_labels_size, color = Sample_labels_color)
            else:

                for target, color in zip(targets,colors):
                    indicesToKeep = Color_by_disc_var == target
                    plt.scatter(ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[0]],ProjectedData.loc[indicesToKeep,list(ProjectedData.columns)[1]], marker='o', color=color, s = 15)
                    
            plt.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            plt.ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            plt.title('2 Components - Observations', fontsize = Title_size)
            plt.legend(targets)

            # plot of loadings
            plt.subplot(1, 2, 2)

            if Arrow_labels == True:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)
                    plt.text(Loadings.iloc[i,0]* (Arrow_labels_shift -.1), Loadings.iloc[i,1] * (Arrow_labels_shift -.1), Loadings.index[i], color=Arrow_labels_color, fontsize = Arrow_labels_size, ha='center', va='center')
            else:
                for i in range(Loadings.shape[0]):
                    plt.arrow(0,0,Loadings.iloc[i,0], Loadings.iloc[i,1],color=Arrow_colors,alpha=0.5,head_width=Arrow_head_size)

            plt.axhline(y=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.axvline(x=0, linestyle='-', linewidth=1.2, color='black', alpha=0.5)
            plt.xlabel('Component 1 ({} %)'.format(round(100*ExplainedVar[0],2)), fontsize = X_label_size)
            plt.ylabel('Component 2 ({} %)'.format(round(100*ExplainedVar[1],2)), fontsize = Y_label_size)
            plt.title('2 Components - Variable Characterization', fontsize = Title_size)
