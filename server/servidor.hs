-- Echo server program
module Main (main) where
import Data.Char (isDigit)
import Control.Concurrent (forkFinally)
import qualified Control.Exception as E
import Control.Monad (unless, forever, void)
import qualified Data.ByteString as S
import qualified Data.List.NonEmpty as NE
import Network.Socket
import Network.Socket.ByteString (recv, sendAll)
import qualified Data.ByteString.Char8 as BC

import System.Environment
import qualified Data.List as L

import qualified Data.Text as T
import qualified Data.Text.Encoding as T

main :: IO ()
main = runTCPServer Nothing "3000" talk
  where
    talk s = do
        msg <- recv s 1024
        unless (S.null msg) $ do
          sendAll s (doP msg <> BC.pack "\n")
          talk s

-- from the "network-run" package.
runTCPServer :: Maybe HostName -> ServiceName -> (Socket -> IO a) -> IO a
runTCPServer mhost port server = withSocketsDo $ do
    addr <- resolve
    E.bracket (open addr) close loop
  where
    resolve = do
        let hints = defaultHints {
                addrFlags = [AI_PASSIVE]
              , addrSocketType = Stream
              }
        NE.head <$> getAddrInfo (Just hints) mhost (Just port)
    open addr = E.bracketOnError (openSocket addr) close $ \sock -> do
        setSocketOption sock ReuseAddr 1
        withFdSocket sock setCloseOnExecIfNeeded
        bind sock $ addrAddress addr
        listen sock 1024
        return sock
    loop sock = forever $ E.bracketOnError (accept sock) (close . fst)
        $ \(conn, _peer) -> void $
            forkFinally (server conn) (const $ gracefulClose conn 3000)

doP bst = deCad (doL (aCad bst))

doL :: String -> String
doL [] = []
doL lin = hazL (takeWhile (/= '\n') lin) ++ doL (drop 1 (dropWhile (/= '\n') lin))

hazL l = menu l

menu msg
  | not (L.all isDigit msg) = "Por favor ingrese un número positivo."
  | n <= 0 = "Por favor ingrese un número positivo."
  | n < 4 = "No hay soluciones para este tamaño"
  | otherwise = show (reinas n)
  where n = read msg :: Int

rev l = L.foldl (#) [] l
  where (#) xs x = x:xs

aCad  = T.unpack . T.decodeUtf8
deCad = T.encodeUtf8 . T.pack

-- N-Reinas Código

estaSegura :: Int -> Int -> [(Int, Int)] -> Bool
estaSegura fila col reinas = 
    not $ L.any (\(f, c) -> f == fila || c == col || abs (f - fila) == abs (c - col)) reinas

colocarReinas :: Int -> Int -> [(Int, Int)] -> [[(Int, Int)]]
colocarReinas n fila reinas
    | fila > n    = [reinas]
    | otherwise   = L.concat [colocarReinas n (fila + 1) (reinas ++ [(fila, col)]) 
                              | col <- [1..n], estaSegura fila col reinas]

convertirSolucion :: [(Int, Int)] -> [Int]
convertirSolucion reinas = L.map snd $ L.sort reinas

resolverNReinas :: Int -> [[(Int, Int)]]
resolverNReinas n = colocarReinas n 1 []

reinas :: Int -> [[Int]]
reinas n = L.map convertirSolucion sols
  where sols = resolverNReinas n
