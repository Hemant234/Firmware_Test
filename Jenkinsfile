node('') {
	
 	stage('checkout'){      
    	   git(
       url: 'https://github.com/Hemant234/jenkins.git',
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
	bat 'xcopy "C:/Program Files (x86)/Jenkins/workspace/Build_machine pull"'
	}
	dir("$workspace_env"){
	bat ''' FOR /f "tokens=*" %%a in ('dir *@tmp /A:D /B') DO RMDIR /S /Q %%a''' 
	}
  }
}
