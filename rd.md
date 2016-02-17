# Spark Tropo
This is a simple application that integrates Tropo with Spark. When a user texts the Tropo number, their text is posted to a specific Spark room. This app is a introductory tutorial to the Tropo Scripting API and Spark Web API. 

## Setup repo
1. Clone this repo onto your machine

## Setup Spark
1. Register on Spark  
  Go to https://web.ciscospark.com/#/signin and enter your email.  
  Cisco will send an email to confirm your email. Then you will set your password.  
  After that it will log you into the Spark chat room.  

  <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24798810500/in/album-72157664637717851/" title="spark_chat"><img src="https://farm2.staticflickr.com/1628/24798810500_7b764bd708.jpg" width="500" height="204" alt="spark_chat"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

2. Get Spark Access Token
  1. Go to https://developer.ciscospark.com
  2. Click **Login**. It should automatically log you in since you already logged in to Spark.
  3. Click the avatar in the right hand upper corner. 
  4. Click **Copy**.  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/undefined/albums/72157664637717851" title="SparkTropo Screenshots"><img src="https://farm2.staticflickr.com/1707/24467330913_88b2803523_m.jpg" width="240" height="71" alt="SparkTropo Screenshots"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  
  5. In heroku/constants.py replace 'Put your token here' on line 19 with your access token.  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24799006740/in/album-72157664637717851/" title="Screen Shot 2016-02-17 at 3.41.28 PM"><img src="https://farm2.staticflickr.com/1441/24799006740_881fe10c7c_m.jpg" width="240" height="67" alt="Screen Shot 2016-02-17 at 3.41.28 PM"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  
  6. Commit your change.

## Setup Tropo
1. Register on Tropo
  1. Go to https://www.tropo.com
  2. Click **Register**
  3. Submit the registration form
  4. Check your email and confirm your account
2. Create new scripting app
  1. Click **Create New App**
  2. Name your app  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24463720214/in/album-72157664637717851/" title="tropo_app_name"><img src="https://farm2.staticflickr.com/1458/24463720214_c6080549c5_n.jpg" width="320" height="102" alt="tropo_app_name"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  
  3. Create new script  
    1. Click on **New script**.
    2. Paste the code from tropo/spark.py, enter the filename and click **Save**.  
       <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24798811030/in/album-72157664637717851/" title="tropo_script"><img src="https://farm2.staticflickr.com/1483/24798811030_d5e373903d_z.jpg" width="640" height="446" alt="tropo_script"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
  
  4. Click **CREATE APP**
3. Add number
  1. Scroll down to the **Numbers** section
  2. Select Country
  3. Select Region
  4. Click **ADD**  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24463720934/in/album-72157664637717851/" title="tropo_number"><img src="https://farm2.staticflickr.com/1487/24463720934_95bf4230d0.jpg" width="500" height="141" alt="tropo_number"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Setup Heroku
1. Sign up or Log in to Heroku: https://www.heroku.com
2. Create new app
  1. Click the + icon in the upper right hand corner.  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24463721004/in/album-72157664637717851/" title="heroku_plus"><img src="https://farm2.staticflickr.com/1630/24463721004_c23d40660b_m.jpg" width="177" height="97" alt="heroku_plus"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
  2. Select **Create new app**
  3. Enter your app name
  4. Select the region for app's runtime (eg. United States or Europe).
  5. Click **Create App**  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24467546563/in/album-72157664637717851/" title="heroku_app"><img src="https://farm2.staticflickr.com/1508/24467546563_3ca3a02d76_z.jpg" width="585" height="417" alt="heroku_app"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

3. Deploy the app.  
  *Note: you should be on the Deploy tab.*  
  <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/25001104871/in/album-72157664637717851/" title="deploy"><img src="https://farm2.staticflickr.com/1693/25001104871_6652e90a39_m.jpg" width="105" height="58" alt="deploy"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  
  
  1. Scroll down to the section **Deploy using Heroku Git**.  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24798811410/in/album-72157664637717851/" title="deploy_git"><img src="https://farm2.staticflickr.com/1604/24798811410_4f0c908d2d_m.jpg" width="180" height="139" alt="deploy_git"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
  
  2. Follow the instructions.  
     *Note: You will not need to enter ```git init``` since the repo was cloned.*
4. Enter heroku app name in Tropo script
  1. On your Tropo app, click **Edit script**
  2. Change the url on line 15 to your Heroku app url  
    <a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24726749279/in/album-72157664637717851/" title="tropo_update"><img src="https://farm2.staticflickr.com/1620/24726749279_4672862614_z.jpg" width="544" height="557" alt="tropo_update"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Play with your app
1. Congratulations! Your app is live.
2. Text the Tropo number and watch your text post in Spark. :)  

### Text  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/24464297944/in/album-72157664637717851/" title="Tropo texting"><img src="https://farm2.staticflickr.com/1626/24464297944_55b58c1f3c.jpg" width="333" height="500" alt="Tropo texting"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

### Chat  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/140391773@N02/25068090126/in/album-72157664637717851/" title="chat_posted"><img src="https://farm2.staticflickr.com/1609/25068090126_9c8f5db8e0_z.jpg" width="640" height="228" alt="chat_posted"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
