import torch.nn as nn


class Net(nn.Module):
    def __init__(self, out_count):
        super(Net, self).__init__()

        self.conv = nn.Sequential(nn.Conv2d(3, 16, (1, 3)),
                                  nn.ReLU(),
                                  nn.Conv2d(16, 32, (1, 3)),
                                  nn.ReLU(),
                                  nn.MaxPool2d(2),
                                  nn.BatchNorm2d(32),
                                  nn.Conv2d(32, 64, (1, 3)),
                                  nn.ReLU(),
                                  nn.MaxPool2d(2),
                                  nn.Conv2d(64, 128, (1, 3)),
                                  nn.ReLU(),
                                  nn.Conv2d(128, 256, (1, 3)),
                                  nn.ReLU(),
                                  nn.BatchNorm2d(256),
                                  nn.Conv2d(256, 256, (3, 3)),
                                  nn.ReLU(),
                                  nn.MaxPool2d(2),
                                  nn.Conv2d(256, 512, (3, 3)),
                                  nn.ReLU(),
                                  nn.MaxPool2d(2),
                                  nn.BatchNorm2d(512))

        self.lstm = nn.LSTM(512, 128, 2, bidirectional=True)

        self.fc = nn.Sequential(nn.Linear(256, 512),
                                nn.ReLU(),
                                nn.Linear(512, 256),
                                nn.ReLU(),
                                nn.LayerNorm([9, 256]),
                                nn.Linear(256, out_count))

    def forward(self, x):
        # print(x.shape)
        conv_out = self.conv(x)
        # print(conv_out.shape)
        conv_out = conv_out.reshape(
            conv_out.shape[0],
            conv_out.shape[1] * conv_out.shape[2],
            conv_out.shape[3]
        )
        # print(conv_out.shape)
        conv_out = conv_out.permute(0, 2, 1)
        # print(conv_out.shape)
        lstm_out, _ = self.lstm(conv_out)
        # print(lstm_out.shape)
        fc_out = self.fc(lstm_out)
        # print(x.shape)
        return fc_out
