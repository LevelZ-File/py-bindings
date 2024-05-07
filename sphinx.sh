git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"
git fetch origin gh-pages

if [ ! -d "out" ]; then
  mkdir out
fi;

cp -Rfv docs/build/* ./out/

git switch -f gh-pages

for dir in ./*
do
  if [ "$dir" == "./out" ]; then
    continue
  fi

  rm -rf "$dir"
done

cp -Rfv ./out/* ./
rm -rf ./out

git add .
git commit -m "Update Sphinx ($1)"
git push -f origin gh-pages