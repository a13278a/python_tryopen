from networks import openSetClassifier


net = openSetClassifier.openSetClassifier(cfg['num_known_classes'], cfg['im_channels'], cfg['im_size'],
										init_weights = not args.resume, dropout = cfg['dropout'])