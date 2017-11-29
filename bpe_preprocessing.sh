#! /bin/bash

export RD="/home/kuznetsov/asi"
export TOPIC="science_and_technology_news"
export SUBWORDDIR="/home/kuznetsov/asi/bpe/subword-nmt/"
export SRCDIR="$RD/preprodata/stage2/youtube/$TOPIC/"
export TGTDIR="$RD/preprodata/stage2.1/youtube/$TOPIC/"



merge_file='merge.txt'
codes_file='codes.txt'
vocab_file='bpeshare.voc'
symbols_count=30000
echo $TGTDIR/$merge_file $TGTDIR
mkdir -p $TGTDIR
mkdir $TGTDIR/txt
echo '' > $TGTDIR/$merge_file
cat $SRCDIR/txt/* >> $TGTDIR/$merge_file

cd $SUBWORDDIR

./learn_bpe.py -s $symbols_count < $TGTDIR/$merge_file > $TGTDIR/$codes_file
./learn_bpe.py -s $symbols_count < $TGTDIR/$merge_file > $TGTDIR/$codes_file
./apply_bpe.py -c $TGTDIR/$codes_file < "$TGTDIR/$merge_file" |./get_vocab.py  >  "$TGTDIR/$vocab_file"

for textfile in $SRCDIR/txt/*
do
infile=$SRCDIR/txt/${textfile##*/}
outfile=$TGTDIR/txt/${textfile##*/}
echo $infile to $outfile
./apply_bpe.py -c $TGTDIR/$codes_file < "$infile" > "$outfile"
done
