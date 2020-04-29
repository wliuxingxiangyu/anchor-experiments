# -*- coding: utf-8 -*-
import subprocess
datasets = ['adult', 'recidivism', 'lending']
explainers = ['anchor', 'lime']
models = ['xgboost', 'logistic', 'nn']
out = 'out_pickles'
for dataset in datasets:
    for explainer in explainers:
        for model in models:
            outfile = '/tmp/%s-%s-%s.log' % (dataset, explainer, model)
            print 'Outfile:', outfile
            # Outfile: /tmp/adult-anchor-xgboost.log           
            
            outfile = open(outfile, 'w', 0)
            cmd = 'python compute_explanations.py -d %s -e %s -m %s -o %s' % (
                dataset, explainer, model,
                '%s/%s-%s-%s' % (out, dataset, explainer, model))#这一行为输出模型文件:out_pickles/adult-anchor-xgboost
            print cmd
            # python compute_explanations.py -d adult -e anchor -m xgboost -o out_pickles/adult-anchor-xgboost  
            subprocess.Popen(cmd.split(), stdout=outfile)
