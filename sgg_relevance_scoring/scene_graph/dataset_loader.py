from abc import ABC, abstractmethod
import os
import json


# Dataset Class
class Dataset:
    def __init__(self, annotation_list, label_map):
        self.annotation_list = annotation_list
        self.label_map = label_map

    def get_annotation_list(self):
        return self.annotation_list
    
    def get_label_map(self):
        return self.label_map
    
    def visualize_dataset(self):
        # TODO: Implement visualization maybe
        pass

# Abstract dataset class
class DatasetLoader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_dataset(self, verbose=True):
        pass

    @abstractmethod
    def _get_dataset_dir(self):
        pass


class SampleDatasetLoader(DatasetLoader):
    def __init__(self):
        super().__init__()

    def load_dataset(self, verbose=True):
        # Get dataset directory
        img_dir, anno_dir = self._get_dataset_dir()

        # Load annotations
        with open(anno_dir + '/scene_validation_annotations.json') as f:
            anno_list = json.load(f)

        if verbose:
            img_count = 0
            for img in os.listdir(img_dir):
                if img.endswith('.png'):
                    img_count += 1
            print(f'Loaded {len(anno_list)} annotations and {img_count} images')

        label_map = {}
        for sample in anno_list:
            if sample['label_name'] not in label_map:
                label_map[sample['label_name']] = sample['label_id']

        if verbose:
            print(f'Loaded {len(label_map)} labels')

        return Dataset(anno_list, label_map)
            

    def _get_dataset_dir(self):
        img_dir = os.path.join(os.path.dirname(__file__), 'ActionGenome/frames_bicls')
        anno_dir = os.path.join(os.path.dirname(__file__), 'ActionGenome/anno_frames_bicls')

        return img_dir, anno_dir
    