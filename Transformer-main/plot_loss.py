import matplotlib.pyplot as plt
import os
def plot_loss(train_losses, val_losses, test_losses, setting):
    folder_path = './loss_graphics/' + setting + '/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    epochs = range(1, len(train_losses) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_losses, label='Training Loss', color='blue', marker='o')
    plt.plot(epochs, val_losses, label='Validation Loss', color='orange', marker='x')
    plt.plot(epochs, test_losses, label='Test Loss', color='red', marker='+')
    plt.title('Epoch vs Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.savefig('./loss_graphics/' + setting + '/epochLoss.png', dpi=300)
    plt.show()
