main = do
  putStrLn "Enter words to reverse:"
  getWords
  
getWords =  do
  line <- getLine
  if null line
    then return ()
    else do
      putStrLn $ reverseWords line
      getWords

reverseWords :: String -> String
reverseWords = unwords . map reverse . words
