
**项目名称**：风雅清新

---
# 0. 使用方法
安装Peddle、PeddleOCR、PyQt等必要库，运行app.py即可。

# 1. 项目背景和意义

中华文明经典古籍是中国文化的重要组成部分，代表了中国传统文化的精髓和智慧。这些古籍具有博大精深的思想、丰富多彩的艺术和历史价值，在一代代人的传承和发扬下早已融入了中华民族的血脉之中。在现代社会，它们是我们了解和认识中国文化传统的重要途径，也是引导和塑造我们的价值观和思维方式的重要源泉，具有重要的意义。通过研读和传承中华文明经典古籍，我们能够更好地理解和应对当代社会面临的挑战，也有助于弘扬中国文化的魅力和影响力。
但在当今数字化时代，传统纸质中华古籍面临着破损腐朽、倒卖流失的风险。除此之外，随着社会发展和文化多元化的趋势，越来越多的人对古籍文化缺乏兴趣和了解，传统文化的价值被逐渐忽视和淡化；许多古籍仍然只存在于纸质文献中，没有数字化和网络化的传播，限制了古籍的传播和推广。基于以上背景，我们希望基于中华古籍原本图片数据集开发一个对古籍的数字化鉴赏和数据统计可视化系统，利用前沿信息技术和数字设计工具深度挖掘中华古代典籍的价值，以数字人文作品的新颖形态创造性地展现古籍的文物性、艺术性和知识性，实现“中华传统文化的创造性转化和创新性应用”，让传承数千年的古籍在新时代“活起来”、在全球的文化舞台上火起来，吸引更多青年投身于对古籍的研究和传承之中。
我们项目的主题是风雅清新，风雅指高雅的品味，清新指清新自然的气息，其意义在于将文明经典古籍中的艺术、文化和自然元素以一种高雅、清新的方式呈现出来，让人在欣赏中感受到古典艺术和自然之美。

# 2. 数据介绍

## 2.1 数据来源

由于Chinavis的比赛数据集已无法找到，我们找到了一本古籍：《庄子故八卷》的原文PDF文件，并对其进行了相应的预处理。

## 2.2 数据描述

《庄子故八卷》原书PDF扫描文件，共二百三十九页，分为八个章节。全书为繁体中文，据我们的统计共五万七千零二十三字。

## 2.3 数据处理

为了方便后续处理，我们首先将古籍进行了图像化处理。通过这一步骤，我们将每一页的内容转换为图像形式，并调整了图片的规格，为后续文字的检测和识别做好准备。接下来，我们对每个图像进行了二值化处理。二值化是一种常见的图像处理方法，它将图像转换为只包含黑白两种颜色的形式。这一步骤对于文字的检测和识别非常重要，因为它可以使文字部分更加清晰和突出，方便后续的自动化处理。为了实现文字的检测和识别，我们采用了PaddleOCR这一先进的工具。PaddleOCR是一个基于深度学习的开源OCR项目，它可以准确地检测和识别图像中的文字内容。我们将每个经过二值化处理的图像输入PaddleOCR，通过其强大的识别能力，我们统计出了不同章节字数出现次数的数据。

# 3. 可视化任务

我们开发了一个对古籍的数字化鉴赏和数据统计可视化系统，利用计算机技术向用户生动展示古籍内容，允许用户对每章节内容进行自由阅读。汉字是承载书籍思想的载体，用户可以检索任意一页中指定汉字出现次数与位置，该功能通过OCR进行实现。我们对汉字出现的次数与分布进行了可视化。首先，我们采用了汉字云的形式，将古籍中的高频汉字以醒目的方式展现给用户。通过这种形式，用户可以直观地了解到古籍中哪些汉字使用频率较高。另外，我们还利用饼图展示了不同章节中字数的占比。这个图表可以让用户一目了然地看到各个章节在整本古籍中所占的比例。通过比较不同章节的字数，用户可以对古籍的结构和篇幅分布有更深入的了解。除此之外，我们还采用堆叠图来展示高频汉字在不同章节中的出现次数。这个图表通过不同颜色的堆叠柱状图，清晰地展示了每个高频汉字在各个章节中的出现情况。用户可以通过这个图表进一步探索古籍中不同汉字的分布规律和重要性。最后，为了实现与用户的互动和自由阅读，我们设计并实现了一个可交互的可视化系统。该系统通过使用Echarts库实现了各种可视化图表，并通过QWebEngineView将这些图表嵌入到系统中。用户可以通过该系统同时阅读古籍原文和浏览可视化图表，从而更深入地理解和鉴赏古籍的内容。

# 4. 评估分析

我们选择了一本古籍资源《庄子故八卷》作为可视化对象，这为系统的实现提供了一个具体的案例。利用图像化处理和二值化处理，将古籍转换为图像形式，并成功地使用PaddleOCR进行文字的检测和识别，并获得了汉字数量及其分布的数据。这一步骤为后续的数据分析和可视化提供了基础。

我们充分利用了汉字出现的次数和分布信息，通过汉字云、饼图和堆叠图等图表形式，直观地展现了古籍中的重要汉字、章节字数占比和高频汉字在不同章节中的出现次数。这些可视化图表不仅美观易懂，而且帮助用户更好地理解古籍的结构。

最后，我们设计并实现了一个可交互的系统，允许用户通过该系统同时阅读古籍原文和浏览可视化图表。这样的设计让用户能够更加自由地探索古籍，并将文字和图表相结合，加深对古籍的理解和鉴赏，使系统的展示效果更加优雅和流畅。

但是，客观来看，我们的工作仍有以下不足：首先，我们的页面设计整体而言尽管达到了使用的目的，但在美观度上存在不足，整体设计也很难和“古籍”与“汉字”这两个主题有效结合。其次，尽管我们进行了数据预处理与数据清洗的工作，受制于OCR模型的准确率与古籍文件本身数据的清晰度，我们挖掘出的数据可能存在一定程度的误差。






