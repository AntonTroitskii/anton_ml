import random
import matplotlib.pyplot as plt


def display_random_images(dataset, n=6, seed=None):

    if seed:
        random.seed(seed)

    if n > 6:
        print('For display purpose, n shoudn\'t be large 6')

    random_img_idx = random.sample(range(len(dataset)), k=n)

    plt.figure(figsize=(16, 8))

    for i, sample in enumerate(random_img_idx):

        img, label = dataset[sample][0], dataset[sample][1]
        img_adjust = img.permute(1, 2, 0)
        plt.subplot(1, n, i+1)
        plt.imshow(img_adjust)
        plt.axis(False)
        plt.title(str(label))


def plot_results(results):
    """Plot grah of Loss (train and test) and accuracy (train and loss)

    Args:
        results (dict[list[float]]): Input a dict dict with result of 'train_loss', 'test_loss', 
'train_acc', 'test_acc'.
    """
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(results['train_loss'], label='train')
    plt.plot(results['test_loss'],  label='test')
    plt.title('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(results['train_acc'], label='train')
    plt.plot(results['test_acc'], label='test')
    plt.title('Acciracy')
    plt.legend()


def save_plot_results(results, file_path):
    plot_results(results=results)
    plt.savefig(file_path)
