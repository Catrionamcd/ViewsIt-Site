## Manual Testing

### Testing for User Stories
*User Stories*
* Site visitor(unauthenticated user) to view list of approved channels.
* Site visitor(unauthenticated user) to view posts in channels.
* Site visitor(unauthenticated user) to view stats for a post, see how many likes there are for that post.

*Steps Taken*
1. Check that once the site is initiated a list of approved posts should appear on the screen for the vistors perusal.
2. The navigation bar should only have the home, register/login, channel list and search options.
3. The functionality to create a channel, a post or a like should not be available to an unauthenticated vistor to the site.

![alt text](assets/test-images/Test-View-Unreg-Screen.png)

4. If a url link exists on a post, the vistor should be able click on this link and the clicked link should open in a separate tab.

5. Check that the number of likes is visible to the visitor.

![alt text](assets/test-images/Test-View-Num-Likes.png)


*Pass/Fail:* **Pass**

*User Story*
* All users of the site to use the search field for author, channel topic or post title.This will help filter the posts for what the users wants to see.

*Steps Taken*

1. Enter an author to search for posts made by this author. I entered 'DavyH' in the search field for this test.

![alt text](assets/test-images/Test-Search-Author.png)

2. Enter a channel topic in search field to search for posts with the topic. I entered 'Music' in the search field for this test.

![alt text](assets/test-images/Test-Search-Title.png)

3. Enter a word to search for posts with this word in the post title or description. I entered 'Surf' in the search field for this test.

![alt text](assets/test-images/Test-Search-Desc.png)

*Pass/Fail:* **Pass**

*User Story*
* Account Registration for site vistor.

*Steps Taken*

1. If a user wants to contribute to the site and post some of their views or even set up their own channel of interest they must register with the site. To test this I created a new user, 'MaryOD'.

![alt text](assets/test-images/Test-Reg.png)

2. Entered different passwords to force an error message.

![alt text](assets/test-images/Test-Unsuccess-Reg.png)

3. Checked to see if the user was set up and that a successful message appears.
4. Checked if x clicked on message, the message will disappear.

![alt text](assets/test-images/Test-Success-Reg.png)

4. Try login as the user.
5. Enter invalid data to ensure only valid users can login.
6. If a authenicated user is logged in ensure that the following extra options appear on the navigation bar to enable extra functionality for a registered user.
    - Channel Manage
    - New Channel
    - Post 

![alt text](assets/test-images/Test-NavBar-User-Extras.png)

7. Test logging out or choosing to stay logged in and going back to site.

![alt text](assets/test-images/Test-Success-Logout.png)

*Pass/Fail:* **Pass**

*User Stories*
* Set up a new channel as a registered user of the site.
* As a super user/administrator the ability to approve a new channel.

*Steps Taken*

1. Test the set up of new channel.
2. Ensure that, if not all the information required is entered, an error message should appear to alert the user. 

![alt text](assets/test-images/Test-New-Channel-Data.png)

3. Ensure a message appears to the user to say that the channel has to be approved once the relevant information is entered and the channel is submitted.

![alt text](assets/test-images/Test-New-Channel.png)

![alt text](assets/test-images/Channel-Setup-Message.png)


4. Ensure that the channel does not appear on the list of channels until it is approved.

![alt text](assets/test-images/Test-Approved-Channels.png)

5. As a super user/administrator update the new channel status to 'published' in the django dashboard.

![alt text](assets/test-images/Test-DashBoard-Channels.png)

![alt text](assets/test-images/Test-Channel-Publish.png)

![alt text](assets/test-images/Test-Channel-Publish-Success.png)


6. Ensure that the new channel now appears in the list of channels.

![alt text](assets/test-images/Test-New-Channel-List.png)


*Pass/Fail:* **Pass**

*User Story*

* As a channel author/owner or super user/administrator edit a channels details. This is done through the Channel Manage option.

*Steps Taken*
1. Choose the Channel Manage option from the navigation bar. 
2. Ensure only the channels owned by the logged in user are available.
![alt text](assets/test-images/Test-Channel-Manage.png)

3. Once the channel details are changed ensure that the channel status is changed to 'Draft' and needs approval again from the super user/administrator.

![alt text](assets/test-images/Test-Channel-Edit.png)

4. This message will appear to the user.

![alt text](assets/test-images/Test-Channel-Approve-Again.png)

5. Check in Django dashboard to see that the channel has beem set back to 'Draft'.

![alt text](assets/test-images/Test-Channel-Draft-Again.png)


*Pass/Fail:* **Pass**

*User Story*

* As a channel author/owner or super user/administrator the functionality to delete a channel.

*Steps Taken*

1. Choose Channel Manage option from the navigation bar. Ensure only the channels attached to the user logged in are available for deletion.

![alt text](assets/test-images/Test-Delete-Channel.png)

2.  Ensure a modal window will appear for delete a channel to ask the user if they are sure that they wish to go ahead with the action.

![alt text](assets/test-images/Test-Delete-Channel-Message.png)

3. Ensure only a channel author/owner can delete their own channel.

![alt text](assets/test-images/Channel-Delete-Message.png)

4. Once a channel is deleted, ensure all posts attached are deleted too.
5.  Channel 'Arts & Crafts' had 2 posts attached, when the channel was deleted the 2 posts were also deleted and they no longer showed on the posts screen. 

*Pass/Fail:* **Pass**

*User Story*
* As a registered user or super user/administrator add posts.

*Steps Taken*

1. Choose Posts from the navigation bar.
2. Ensure all approved channels are in drop down options for channels.

![alt text](assets/test-images/Test-Channel-Select.png)

3. Enter data in all fields.

![alt text](assets/test-images/Test-New-Post-Navbar.png)

4. Ensure the correct message is displayed - needing approval from the channel author/owner.
5. Ensure all information added is on the post.
6. Ensure that the post has a shaded background colour until it is approved by the channel author/owner.

![alt text](assets/test-images/Test-New-Post-Message.png)

*Pass/Fail:* **Pass**

*User Story*
* As an owner of a channel the ability to approve channel posts.

*Steps Taken*
1. Choose Channel Manage option from navigation bar.

![alt text](assets/test-images/Test-Channel-Manage.png)

2. Click approve posts
3. The posts awaiting approval should be displayed.
4. Click the approve button.

![alt text](assets/test-images/Test-Post-Approve-Button.png)

5. Click home button to view the post displayed with all other approved post. The background colour should now be white.
6. If the user logged in is the author of the post an Edit and Delete button should appear on the post to enable the author to change or delete the post. 

![alt text](assets/test-images/Test-Post-Channel-Owner.png)

7. If the user logged in is not the author of the post the Edit and Delete buttons should not be displayed.

![alt text](assets/test-images/Test-Approve-Colour.png)


*Pass/Fail:* **Pass**

*User Story*

* As a post author or super user/administrator edit posts.

*Steps Taken*
1. A post may only be edited by the author of the post.
2. Ensure an Edit button appears for all posts created by the author logged in.
3. When the Edit button is clicked all fields in that post can be changed. In this case I changed the post text to add 'Click on the link for a free pattern'.

![alt text](assets/test-images/Test-Post-Edit.png)

4. When the submit button is clicked to update the changes to the post a message should appear to inform the user that the changes are updated but the post needs aprroval from the channel owner again.

![alt text](assets/test-images/Test-Post-Change-Message.png)

5. The background is shaded again and a message letting the user know that the post needs approval appears on the post.

*Pass/Fail:* **Pass**

*User Story*

* As a post author or super user/administrator delete posts.

*Steps Taken*

1. A post may only be deleted by the post author. Ensure the Delete button only appears on the posts created by the user logged in.
2. Both approved and un-approved posts may be deleted.

![alt text](assets/test-images/Test-Post-Delete.png)

![alt text](assets/test-images/Test-Post-Delete-Approve.png)

*Pass/Fail:* **Pass**

*User Story*

* As a user to like/unlike posts and comments.

*Steps Taken*

1. A registered user of the site can 'like' any post.

2. Click on the heart at the end of the post.

3. Ensure the heart turns to a solid red and the number of likes increases by one.

4. If the same user clicks the heart again, the number of likes should decrease by one. 

![alt text](assets/test-images/Test-Post-Likes.png)

*Pass/Fail:* **Pass**

### Validator Testing

## CSS
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
![alt text](assets/images/ViewsIt-CSS-Validator.png)

## HTML
[Nu Html Checker Validator](https://validator.w3.org/)
![alt text](assets/images/ViewsIt-HTML-Validation.png)
![alt text](assets/images/Account-Register-Html-Validation.png)
![alt text](assets/images/Channel-Form-Html-Validation.png)
![alt text](assets/images/Channel-List-Html-Validation.png)
![alt text](assets/images/Channel-Manage-Html-Validation.png)
![alt text](assets/images/Channel-Post-Html-Validation.png)
![alt text](assets/images/Channel-View-Html-Validation.png)
![alt text](assets/images/User-Login-Html-Validation.png)
![alt text](assets/images/User-Logout-Html-Validation.png)

## Javascript
[JShint](https://jshint.com/)
There is some Javascript code within the base.html file. The code was taken from the Code Institute for the message timeout function and MdBootstrap,
https://mdbootstrap.com/docs/standard/extended/back-to-top/ for the back to the top bottom at the end of the screen.

## Python
* Admin.py

![alt text](assets/images/ViewsIt-AdminPy-Validation.png)

* Apps.py

![alt text](assets/images/ViewsIt-AppsPy-Validation.png)

* Forms.py

![alt text](assets/images/ViewsIt-FormsPy-Validation.png)

* Models.py

![alt text](assets/images/ViewsIt-ModelsPy-Validation.png)

* Urls.

![alt text](assets/images/ViewsIt-UrlsPy-Validation.png)

* Views.py

![alt text](assets/images/ViewsIt-ViewsPy-Validation.png)

