import FWCore.ParameterSet.Config as cms

#
#
# Conversion Track candidate producer 
from RecoEgamma.EgammaPhotonProducers.conversionTrackCandidates_cfi import *
# Conversion Track producer  ( final fit )
from RecoEgamma.EgammaPhotonProducers.ckfOutInTracksFromConversions_cfi import *
from RecoEgamma.EgammaPhotonProducers.ckfInOutTracksFromConversions_cfi import *
ckfTracksFromConversions = cms.Sequence(conversionTrackCandidates*ckfOutInTracksFromConversions*ckfInOutTracksFromConversions)

mustacheConversionTrackCandidates = conversionTrackCandidates.clone()
mustacheConversionTrackCandidates.scHybridBarrelProducer = cms.InputTag('particleFlowSuperClusterECAL:particleFlowSuperClusterECALBarrel')
mustacheConversionTrackCandidates.bcBarrelCollection = cms.InputTag('particleFlowClusterECAL')
mustacheConversionTrackCandidates.scIslandEndcapProducer = cms.InputTag('particleFlowSuperClusterECAL:particleFlowSuperClusterECALEndcapWithPreshower')
mustacheConversionTrackCandidates.bcEndcapCollection = cms.InputTag('particleFlowClusterECAL')

ckfOutInTracksFromMustacheConversions = ckfOutInTracksFromConversions.clone()
ckfOutInTracksFromMustacheConversions.src = cms.InputTag('mustacheConversionTrackCandidates','outInTracksFromConversions')
ckfOutInTracksFromMustacheConversions.producer = cms.string('mustacheConversionTrackCandidates')
ckfOutInTracksFromMustacheConversions.ComponentName = cms.string('ckfOutInTracksFromMustacheConversions')

ckfInOutTracksFromMustacheConversions = ckfInOutTracksFromConversions.clone()
ckfInOutTracksFromMustacheConversions.src = cms.InputTag('mustacheConversionTrackCandidates','inOutTracksFromConversions')
ckfInOutTracksFromMustacheConversions.producer = cms.string('mustacheConversionTrackCandidates')
ckfInOutTracksFromMustacheConversions.ComponentName = cms.string('ckfInOutTracksFromMustacheConversions')

ckfTracksFromMustacheConversions = cms.Sequence(mustacheConversionTrackCandidates*ckfOutInTracksFromMustacheConversions*ckfInOutTracksFromMustacheConversions)
