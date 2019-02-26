node() {
	
 	stage('checkout'){      
      	   git(
       url: 'https://github.com/Hemant234/Firmware_Test.git',
       credentialsId: '	d5810384-46fe-4a24-a05b-0f7eefcea946',
       branch: "master"
    )
	}
	stage('setup'){
	powershell 'pwd'
	//shorttime= bat(returnStdout: true, script: "prompt $t$g")
	def date = new Date()
	date=date.format("yyMMdd.HHmm", TimeZone.getTimeZone('IST'))
	println date
	workspace_env= env.WORKSPACE
	dir ("$date") 
	{
	shortCommit = bat(returnStdout: true, script: "git log -1")
	writeFile file: "Commitversion.txt", text: "$shortCommit"
	bat 'xcopy "C:/Program Files (x86)/Jenkins/workspace/gitpull"'
	}
	dir("$workspace_env"){
	bat ''' FOR /f "tokens=*" %%a in ('dir *@tmp /A:D /B') DO RMDIR /S /Q %%a''' 
	}
  }

stage('build env'){	
 def workspace = pwd()
 print "$workspace"
 bat '''cd C:/Python27/Scripts
 set https_proxy=http://165.225.104.32:80
 pip install virtualenv
 cd C:/Program Files (x86)/Jenkins/workspace
virtualenv myproj 
   '''
  }
  	
stage('install '){ 
	//pip install selenium
	//pip install pymodbus
	//pip install pymodbustcp
	//pip install pandas
	//pip install styleframe
	//pip install wxpython
	//pip install win-inet-pton
	//pip install opencv-python
	//pip install python-appium-client"
	}
try{
bat''' robocopy "C:/Program Files (x86)/Jenkins/workspace/gitpull" "C:/Jenkins" /S '''
}
catch(err){}
stage('running the program'){
	dir('C:/Jenkins'){
        bat ''' FOR /f "tokens=*" %%a in ('dir *@tmp /A:D /B') DO RMDIR /S /Q %%a'''
	commit= bat(returnStdout: true, script: '''@for /f "delims=" %%i in ('dir /b /ad "*" 2^>nul') do @cd C:/Jenkins/%%i & cd''').split()
	 }
	 echo "${commit} "
        commit.each {
        //println "${it}"
        dir("${it}"){
	try{
	file=bat(returnStdout: true, script:'''dir /s /b *.txt*''').trim()
	bat '''
        call activate
	IFE_performance.py
	'''
	}
	catch(err){
	echo " no file"
	}
	}
	
 	}
	}
	
}
