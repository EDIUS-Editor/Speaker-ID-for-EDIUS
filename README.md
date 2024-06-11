# Speaker ID for EDIUS

Here, I will share my Python scripts to speed up my video editing on EDIUS software.

## Introduction

My first script is designed to create speaker ID markers for Acoustica (Acon Digital) and EDIUS. Acoustica has automatic speech recognition and transcription capabilities, but Whisper provides superior results. In addition to caption text, captions can be associated with different actors (speaker IDs), and each actor can be assigned a unique color. However, this process needs to be done manually.

To streamline this workflow, I use WhisperX, developed by m-bain. WhisperX is a cutting-edge extension of OpenAI's Whisper model, enhancing it with advanced features like word-level timestamps and speaker diarization.

## WhisperX GUI

You will find a Python file `WhisperX_GUI.py` that helps control WhisperX [here](https://github.com/m-bain/whisperX). I encountered issues with other WhisperX GUI scripts on GitHub, specifically with getting the speaker diarization from pyannote-audio to work on my PC. Therefore, I created my own.

### Installation

If you need help installing WhisperX on your PC, refer to the instructions [here](https://github.com/Pikurrot/whisper-gui). Additionally, you may find this PDF file helpful: [Install WhisperX on Windows](https://github.com/ycyy/faster-whisper-webui/blob/main/docs/windows/install_win10_win11.pdf).

### Hugging Face Token

To enable speaker diarization, you must create a Hugging Face account and include your Hugging Face access token (read). Generate your token from [here](https://huggingface.co/settings/tokens) and accept the user agreement for the following models: Segmentation and Speaker-Diarization-3.1.

### Usage

If you have successfully installed Python, Conda, FFMPEG, Pytorch, Pyannote-audio, WhisperX, etc., then my GUI script should work by simply double-clicking on it.

The GUI is self-explanatory:

1. Select an audio file
2. Select a text file containing your Hugging Face access token
3. Select your model (tiny, base, small, medium, large, large-v2, large-v3)
4. Click Run to generate a .srt and .json file

If the model is not present in your .cache folder, it will first be downloaded automatically by WhisperX, making your first run slower.

### Tips

- **Memory and Performance:** If you are low on memory or require faster processing, consider downgrading from medium to tiny models to trade off accuracy for performance.
- **Batch Size:** Choose a higher batch size to improve performance with a powerful GPU. Lower the batch size if you encounter CUDA memory issues.
- **Compute Type:** float16 is the recommended value. Downgrade to int8 if you experience CUDA memory issues, though this may reduce accuracy.

## WhisperX JSON to Acoustica Captions GUI

After running WhisperX, you should have multiple output files, such as .srt subtitles and a .json data file. My `WhisperX_json_to_Acoustica_Captions_GUI.py` script converts this .json data file into an Acoustica Captions file, which will display subtitles along with speaker ID labels on color markers.

### Usage

1. Double-click on the `WhisperX_json_to_Acoustica_Captions_GUI.py` script.
2. Import the .json data file.
3. Click Run to convert it into an Acoustica Captions .captions file.
4. Import this new .captions file into Acoustica.

After importing the .captions file into Acoustica, you can check the accuracy of the captions and actor (speaker ID) labels. Each actor can be assigned a unique color and name. You can make changes and then export the data as EDIUS markers.

## Conclusion

These scripts aim to enhance your workflow with EDIUS and Acoustica by integrating advanced features from WhisperX. If you encounter any issues or have suggestions for improvement, feel free to contribute or reach out.

Happy editing!
