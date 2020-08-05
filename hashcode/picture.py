def v_photos_merger(photo, photos):
    photo_index = photos.index(photo)
    for item in photos:
        if not item or item == photo:
            continue
        # trying to merge each two V pics
        if can_be_merged(photo,item):
            item_index = photos.index(item)
            photos[item_index] = None
            photos[photo_index] = None
            return 'V ' + str(photo_index) + ',' + str(item_index) + " " + tags_merger(photo,item)
    return None
#  search for next possible next slides in the list for the current
def search_for_next_photo(photo, photos):
    possible_merges = []
    for item in photos:
        if not item == photo and can_be_merged(photo,item):
            possible_merges.append(item)
    return possible_merges
# see it two V pics can be merged
def can_be_merged(photo,item):
    photo_tags, item_tags = tags_splitter(photo, item)
    for tag in photo_tags:
        if tag in item_tags:
            return True
    return False
# find the max merge points
def max_transition_points(pic, possible_merges):
    points = 0
    best_guess = None
    # for each possible pic
    for transistion in possible_merges:
        photo_tags, item_tags = tags_splitter(pic, transistion)
        tags_in_common = 0
        # cal. the tags points and the remaining tags in each pics
        for tag in photo_tags[:]:
            if tag in item_tags:
                tags_in_common += 1
                item_tags.remove(tag)
                photo_tags.remove(tag)
        trans_points = min(tags_in_common,len(item_tags), len(photo_tags))
        # if the trans_points is bigger than our current max. change it
        if points < trans_points:
            points = trans_points
            best_guess = transistion
    return best_guess

# merge the tags of two V pictures
def tags_merger(photo,item):
    photo_tags, item_tags = tags_splitter(photo, item)
    return ' '.join(set(photo_tags + item_tags))

# parse the tags from each pic
def tags_splitter(photo1, photo2):
    return photo1.split(" ")[2:], photo2.split(" ")[2:]
#  c_memorable_moments, a_example, b_lovely_landscapes, d_pet_pictures,e_shiny_selfies
with open("input/a_example.txt","r") as input:
    n = input.readline().strip("\n")
    photos = input.read().splitlines()

new_copy = []
for photo in photos:
    if not photo:
        continue
    if photo.startswith("H"):
        # reformat the H pictures to contain its index so i can print it to the output
        new_copy.append("H " + str(photos.index(photo)) + photo[3:])
    else:
        #  find the possible images to be merged with this pic
        possible_merge = v_photos_merger(photo, photos)
        if possible_merge:
            # adding it to the list after reformating it 
            new_copy.append(possible_merge)        
# print(new_copy)
output = []
output.append(new_copy[0])
last_item_in_slides = new_copy[0]
new_copy[0]=""
# for the number of slides take the last slide always and search for the next slide
for index in range(len(new_copy)):
    # search for the next possible slides that can be added in the output
    if not last_item_in_slides:
        break
    possible_merges = search_for_next_photo(last_item_in_slides, new_copy)
    # select the most intersting slide in the collection
    last_item_in_slides = max_transition_points(last_item_in_slides, possible_merges)
    # adding the slide to the output and delte the slide form the input so no duplicate slides appears
    if last_item_in_slides:
        new_copy[new_copy.index(last_item_in_slides)] = ""
        output.append(last_item_in_slides)

# print(len(output))
output_file = open("output.txt", "w")
for slide in output:
    output_file.write(slide.split(" ")[1])
    output_file.write("\n")
output_file.close()
