# Bee Detection

## Processing Images

### Extracting Images
1. Open the track in VLC Media player
2. Press `e` to go forward one frame
3. Once a bee going into a hole is present in the frame, press `shift + s` to capture the frame

To edit where images are saved, go to `tools -> preferences -> video -> video snapshots` and change the `Directory` variable.

### Annotating Images
1. Open LabelImg by going to `C:/Users/user/labelImg` and opening `labelImg.exe`
2. Click `Open Dir` and navigate to where the images are located. [**Important**: Add new images to the `new_images` directory so that old images are re-annotated]
3. Change where the annotations are saved by pressing `ctrl + r` and navigating to the `annotations` folder
4. Press `ctrl + n` to create a new label
5. To save the annotation, press `ctrl + s` (Not necessary)
6. Once all bees have been labelled, click on `Next Image`
7. Move images back to `images` from `new_images`
8. Rename `bee-detection\new_images` to `bee-detection\images`
9. Rename `<folder>new_images</folder>` to `<folder>images</folder>`
9. Run `scripts/xml_to_csv.py`

