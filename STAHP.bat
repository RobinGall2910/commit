@echo off
cls
echo   ******** **********     **       **      **   ******* 
echo  **////// /////**///     ****     /**     /**  /**////**
echo /**           /**       **//**    /**     /**  /**   /**
echo /*********    /**      **  //**   /**********  /******* 
echo ////////**    /**     **********  /**//////**  /**////  
echo        /**    /**    /**//////**  /**     /**  /**      
echo  ********     /**    /**     /**  /**     /**  /**      
echo ////////      //     //      //   //      //   //       

:start
set i=0
set j=0

:loop1
    color %j%%i%
    
    set /A i+=1
    if "%i%" == "10" (
        set i=0
        goto loop2
    ) else (
        goto loop1
    )
:loop2
    set /A j+=1
    if "%j%" == "10" (
        goto start
    ) else (
        goto loop1
    )
goto start
